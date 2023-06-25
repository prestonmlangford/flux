
def c_repr_expr(expr):
    if expr["tag"] == "ref":
        return "self->" + ".".join(expr["path"])
    elif expr["tag"] == "const":
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
    else:
        return "PMLFIXME"

def c_repr_process_func(module):
    s = ""
    for var in module["vars"]:
        if (var["tag"] == "module") or (var["tag"] == "block"):
            tag = var["tag"]
            name = var["name"]
            type = var["type"]
            s += f"static void process_{name}(struct {type}* self)\n"
            s += "{\n"
            s += f"    struct {type}* {name} = &(self->{name});\n\n"
            for con in var["cons"]:
                field = con["name"]
                expr = c_repr_expr(con["expr"])
                s += f"    {name}->{field} = {expr};\n"
            
            s += "\n"
            s += f"    {tag}_{type}({name});\n"
            s += "}\n\n"
    
    return s

def c_repr_module_func(module):
    type = module["type"]
    s = f"void module_{type}(struct {type}* self)\n"
    s += "{\n"
    for var in module["vars"]:
        if var["tag"] == "in": continue
        name = var["name"]
        s += f"    process_{name}(self);\n"
    s += "}\n\n"
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
    
    s += "}\n\n"
    
    return s
