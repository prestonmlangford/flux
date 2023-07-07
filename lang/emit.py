
def c_repr_expr_simple(expr):
    tag = expr["tag"]

    if tag == "ref":
        # PMLFIXME this thinks constant values are references
        # the desiged behavior will be to treat them as a namespace value
        return "self->" + ".".join(expr["path"])

    elif tag == "literal":
        type = expr["type"]
        val = expr["val"]

        if type == "bool":
            return "true" if val == 1 else "false"
        else:
            post = ""

            if "u" in type:
                post = "U"

            if "64" in type:
                post += "LL"

            return f"{val}{post}"

    elif tag == "namespace":
        mod = expr["mod"].upper()
        name = expr["name"]
        
        return f"{mod}_{name}"

    else:
        return "PMLFIXME"

def c_repr_eval_op(module,path,name_var,op):
    type_self = module["type"]
    type_var = "PMLFIXME" # PMLFIXME the type needs to be determined from the op and it's arguments
    name_op = op["name"]

    decls = ""
    impls = ""
    fname = f"eval_{name_var}"
    body = ""

    for idx in path:
        fname += f"_{idx}"

    body += f"static {type_var} {fname}(struct {type_self}* self)\n"
    body += "{\n"
    body += f"    {type_var} argv[] = \n"
    body +=  "    {\n"
    for idx,arg in enumerate(op["args"]):
        decl, impl, rhs = c_repr_expr(module, path + [idx], name_var, arg)
        decls += decl
        impls += impl
        body += f"        {rhs},\n"

    body +=  "    };\n"
    body +=  "    size_t argc = COUNT(argv);\n\n"
    body += f"    return {type_var}_{name_op}(argc, argv);\n"
    body += "}\n\n"

    decls += f"static {type_var} {fname}(struct {type_self}* self);\n"
    impls += body

    return decls, impls, (fname + "(self)")

def c_repr_expr(module,path,name_var,expr):
    decls = ""
    impls = ""
    
    tag = expr["tag"]
    
    if tag == "op":
        decls,impls,rhs = c_repr_eval_op(module,path,name_var,expr)
    else:
        rhs = c_repr_expr_simple(expr)

    return decls, impls, rhs

def c_repr_process_mod(module,var):
    name_mod = var["name"]
    type_self = module["type"]
    type_mod = var["type"]
    
    decls = ""
    impls = ""
    fname = f"process_{name_mod}"
    body = ""

    body += f"static void {fname}(struct {type_self}* self)\n"
    body += "{\n"
    body += f"    struct {type_mod}* {name_mod} = &(self->{name_mod});\n\n"
    for con in var["cons"]:
        name_con = con["name"]
        name_var = f"{name_mod}_{name_con}"
        expr = con["expr"]
        decl,impl,rhs = c_repr_expr(module,[],name_var,expr)
        decls += decl
        impls += impl
        body += f"    {name_mod}->{name_con} = {rhs};\n"

    body += "\n"
    body += f"    module_{type_mod.lower()}({name_mod});\n"
    body += "}\n\n"

    decls += f"static void {fname}(struct {type_self}* self);\n"
    impls += body

    return decls, impls, fname

def c_repr_module_impl(module):
    decls = ""
    impls = ""
    body = ""
    for var in module["vars"]:
        vname = var["name"]
        tag = var["tag"]
        if tag == "mod":
            decl,impl,fname = c_repr_process_mod(module,var)
            decls += decl
            impls += impl
            body += f"    {fname}(self);\n"
        elif (tag == "var") or (tag == "out"):
            decl,impl,rhs = c_repr_expr(module,[],var["name"],var["expr"])
            decls += decl
            impls += impl
            body += f"    self->{vname} = {rhs};\n"

    type_mod = module["type"]
    s = f"#include \"{type_mod.lower()}.h\"\n\n"
    s += decls
    s += "\n"
    s += impls
    s += f"void module_{type_mod.lower()}(struct {type_mod}* self)\n"
    s += "{\n"
    s += body
    s += "}\n\n"

    return s

def c_repr_var_decl(var):
    tag = var["tag"]
    type = var["type"]
    name = var["name"]
    try:
        size = var["size"]
    except:
        size = None

    s = ""
    
    if tag == "mod":
        s += "struct "
    
    s += f"{type} {name}"

    if size:
        s += f"[{size}]"

    return s

def c_repr_module_struct(module):
    inputs = []
    states = []
    outputs = []
    
    for var in module["vars"]:
        tag = var["tag"]

        if tag == "in":
            inputs.append(var)
        elif tag == "out":
            outputs.append(var)
        else:
            states.append(var)

    type = module["type"]
    s = f"struct {type}\n"
    s += "{\n"
    s += "\n    /* inputs */\n"
    for input in inputs:
        decl = c_repr_var_decl(input)
        s += f"    {decl};\n"

    s += "\n    /* states */\n"
    for state in states:
        decl = c_repr_var_decl(state)
        s += f"    {decl};\n"

    s += "\n    /* outputs */\n"
    for output in outputs:
        decl = c_repr_var_decl(output)
        s += f"    {decl};\n"
    
    s += "};\n\n"
    
    return s

def c_repr_module_header(module):
    type = module["type"]
    header = type.upper()
    s =  f"#ifndef {header}_H\n"
    s += f"#define {header}_H\n"
    s += "#include <types.h>\n\n"

    s += c_repr_module_struct(module)

    s += f"#endif /* {header}_H */\n"

    return s
