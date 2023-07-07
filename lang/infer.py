from walk import Walker

class Constants(Walker):

    def go(node):
        w = Constants()
        w.scope = {}
        w.parent = ["decl"]
        w.child = ["const"]
        w.walk(node)
        return w.scope

    def visit(self,decl,const):
        decl_type = decl["type"]
        const_name = const["name"]
        name = f"{decl_type}::{const_name}"
        self.scope[name] = const

class Constants(Walker):

    def go(node):
        w = Constants()
        w.scope = {}
        w.parent = ["decl"]
        w.child = ["const"]
        w.walk(node)
        return w.scope
    
    def visit(self,decl,const):
        decl_type = decl["type"]
        const_name = const["name"]
        name = f"{decl_type}::{const_name}"
        self.scope[name] = const

class Locals(Walker):

    def go(node):
        w = Locals()
        w.scope = {}
        w.parent = ["impl"]
        w.child = ["const","in","var","mod"]
        w.walk(node)
        return w.scope
    
    def visit(self,impl,var):
        if var["tag"] == "mod":
            mod_name = var["name"]
            for con in var["cons"]:
                in_name = con["name"]
                

def infer_scope(decls,impl):
    scope = {}

    for var in impl["vars"]:
        tag_var = var["tag"]
        name_var = var["name"]
        type_var = var["type"]
        if (tag_var == "in") or (tag_var == "var"):
            size_var = var["size"]
            scope[name_var] = (tag_var,type_var,size_var)
        elif tag_var == "mod":
            try:
                decl = decls[type_var]
            except:
                raise RuntimeError(f"Type {type_var} not in scope")
            for mod_var in decl["vars"]:
                mod_var_tag = mod_var["tag"]
                if mod_var_tag == "out":
                    mod_var_name = mod_var["name"]
                    scope[f"{name_var}.{mod_var_name}"] = (mod_var_tag,mod_var["type"],mod_var["size"])
    
    return scope


def infer_op_types_old(decls,impl):
    for var in impl["vars"]:
        tag = var["tag"]
        if tag == "in": continue
        if tag == "mod":
            decl = decls[var["type"]]
            for con in var["cons"]:
                for decl_var in decl["vars"]:
                    if (decl_var["tag"] == "in") and (decl_var["name"] == con["name"]):
                        expr = con["expr"]
                        if expr["tag"] == "op":
                            expr["type"] = decl_var["type"]

        if (tag == "var") or (tag == "out"):
            expr = var["expr"]
            if expr["tag"] == "op":
                expr["type"] = var["type"]
