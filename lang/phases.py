from walk import Walker

class GrammarError(Exception): pass

def none(thing): return thing is None
def some(thing): return not none(thing)

# no expressions for inputs
class Ban_Input_Expressions(Walker):

    def go(top):
        w = Ban_Input_Expressions()
        w.parent = ["impl"]
        w.child = ["in"]
        w.walk(top)

    def visit(self,_,var):
        if some(var["expr"]):
            raise GrammarError("Expressions are not allowed for module input variables")

# no expressions for declaration variables
class Ban_Decl_Expressions(Walker):

    def go(top):
        w = Ban_Input_Expressions()
        w.parent = ["decl"]
        w.child = []
        w.walk(top)

    def visit(self,impl,var):
        if some(var["expr"]):
            raise GrammarError("Expressions are not allowed for module declaration variables")

class Build_Decls(Walker):
    def go(top):
        w = Build_Decls()
        w.decls = {}
        w.parent = ["top"]
        w.child = ["decl"]
        w.walk(top)
        top["decls"] = w.decls

    def visit(self,_,decl):
        name = decl["type"]
        decl["_in"] = {}
        decl["_out"] = {}
        self.decls[name] = decl

class Build_Decl_IO(Walker):
    def go(top):
        w = Build_Decl_IO()
        w.parent = ["decl"]
        w.child = ["in","out"]
        w.walk(top)

    def visit(self,decl,var):
        name = var["name"]
        
        if var["tag"] == "in":
            decl["_in"][name] = var
        
        if var["tag"] == "out":
            decl["_out"][name] = var

class _Build_Scope_Refs(Walker):
    def visit(self, impl, var):
        if var["tag"] == "mod":
            mod_type = var["type"]
            mod_name = var["name"]
            try:
                decl = self.decls[mod_type]
            except:
                raise GrammarError(f"No declaration for module {mod_type}")
            for key,val in decl["_out"].items():
                name = f"{mod_name}.{key}"
                impl["_scope"][name] = val
        else:
            name = var["name"]
            impl["_scope"][name] = var

class Build_Impl_Scope(Walker):
    def go(top):
        w = Build_Impl_Scope()
        w.parent = ["top"]
        w.child = ["impl"]
        w.walk(top)
    
    def visit(self, top, impl):
        impl["_scope"] = {}
        w = _Build_Scope_Refs()
        w.decls = top["decls"]
        w.parent = ["impl"]
        w.child = ["in","var","mod"]
        w.walk(impl)

# no expressions for declaration variables
class Build_Module_Connections(Walker):
    def go(top):
        w = Build_Module_Connections()
        w.decls = top["decls"]
        w.parent = ["mod"]
        w.child = ["connect"]
        w.walk(top)

    def visit(self,mod,con):
        mod_type = mod["type"]
        con_name = con["name"]
        try:
            decl = self.decls[mod_type]
        except:
            raise GrammarError(f"Undeclared module type {mod_type}")

        try:
            var = decl["_in"][con_name]
        except:
            raise GrammarError(f"{con_name} is not an input to module {mod_type}")

        con["type"] = var["type"]
        con["size"] = var["size"]

class Validate_Var_Refs(Walker):
    def go(top):
        w = Validate_Var_Refs()
        
        w.parent = []
        w.child = ["var_ref"]
        w.walk(top)

    def visit(self,_,ref):
        name = ref["name"]
        try:
            var = self.vars[name]
        except:
            raise GrammarError(f"Variable {name} is not in scope")

        ref["type"] = var["type"]
        ref["size"] = var["size"]

class Build_Local_Modules(Walker):
    def go(top):
        w = Build_Local_Modules()
        w.mods = {}
        w.parent = ["impl"]
        w.child = ["mod"]
        w.walk(top)
        return w.vars

    def visit(self,impl,mod):
        name = mod["name"]
        self.mods[name] = mod

class Validate_Mod_Refs(Walker):
    def go(top):
        w = Validate_Mod_Refs()
        w.vars = Build_Local_Modules.go(top)
        w.parent = []
        w.child = ["mod_ref"]
        w.walk(top)

    def visit(self,_,ref):
        mod_name = ref["module"]
        out_name = ref["output"]
        try:
            var = self.mods[mod_name]
        except:
            raise GrammarError(f"Module {mod_name} is not in scope")
        
        
        ref["type"] = var["type"]
        ref["size"] = var["size"]

class Validate_References(Walker):
    def go(top):
        w = Validate_References()
        w.parent = ["top"]
        w.child = ["impl"]
        w.walk(top)
    
    def visit(self, top, impl):
        Validate_Var_Refs.go(impl)