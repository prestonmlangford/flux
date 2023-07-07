

def c_repr_expr(expr):
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
    
    elif tag == "op":
        name = expr["name"]
        args = expr["args"]
        
        return f"{name}({args})"
    else:
        return "PMLFIXME"

def c_repr_eval_op(module,path,var):
    type_self = module["type"]
    eval_name = var["name"]
    
    return ""

def c_repr_process_mod(module,var):
    name = var["name"]
    type_self = module["type"]
    type_mod = var["type"]
    
    s = ""
    for con in var["cons"]:
        expr = con["expr"]
        tag = expr["tag"]
        if tag == "op":
            s += c_repr_eval_op(module,[],var)

    s += f"static void process_{name}(struct {type_self}* self)\n"
    s += "{\n"
    s += f"    struct {type_mod}* {name} = &(self->{name});\n\n"
    for con in var["cons"]:
        field = con["name"]
        expr = c_repr_expr(con["expr"])
        s += f"    {name}->{field} = {expr};\n"
    
    s += "\n"
    s += f"    module_{type}({name});\n"
    s += "}\n\n"
    
    return s

def c_repr_static_module_funcs(module):
    s = ""
    for var in module["vars"]:
        tag = var["tag"]
        if tag == "mod":
            s += c_repr_process_mod(module,var)
        elif (tag == "var") or (tag == "out"):
            if var["expr"]["tag"] == "op":
                s += c_repr_eval_op(module,[],var)
    return s

def c_repr_public_module_func(module):
    type = module["type"]
    s = f"void module_{type.lower()}(struct {type}* self)\n"
    s += "{\n"
    for var in module["vars"]:
        tag = var["tag"]
        name = var["name"]
        if tag == "mod":
            s += f"    process_{name}(self);\n"
        elif (tag == "var") or (tag == "out"):
            s += f"    self->{name} = eval_{name}(self);\n"
    s += "}\n\n"
    return s

def c_repr_module_implementation(module):
    header = module["type"].lower()
    s = f"#include \"{header}.h\"\n\n"
    s += c_repr_static_module_funcs(module)
    s += c_repr_public_module_func(module)
    return s

def c_repr_type(t):
    base_types = {
        "u8" : "uint8_t",
        "i8" : "int8_t",
        "u16" : "uint16_t",
        "i16" : "int16_t",
        "u32" : "uint32_t",
        "i32" : "int32_t",
        "u64" : "uint64_t",
        "i64" : "int64_t"
    }
    
    try:
        return base_types[t]
    except:
        return t

def c_repr_var_decl(var):
    tag = var["tag"]
    type = c_repr_type(var["type"])
    name = var["name"]
    try:
        size = var["size"]
    except:
        size = None

    s = ""
    
    if tag == "block" or tag == "module":
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
    s += "#include <stdint.h>\n\n"

    s += c_repr_module_struct(module)

    s += f"#endif /* {header}_H */\n"

    return s
