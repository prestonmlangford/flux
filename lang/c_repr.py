import sys
from walk import Walker

class Emit_C_Repr(Walker):
    def go(top):
        w = Emit_C_Repr()
        w.consts = top["_consts"]
        w.eval_name = ""
        w.expr = []
        w.includes = []

        w.walk(top)
    
    def set_path_depth(self):
        self.path_depth = len(self.get_path())
    
    def get_path_depth(self):
        return self.path_depth
    
    def visit_decl(self, node):
        self.includes.append(node["type"])
        pass

    def visit_impl(self, impl):
        self.scope = {**impl["_scope"], **self.consts}
        self.impl_type = impl["type"]
        header = self.impl_type.upper()
        file = self.impl_type.lower()
        
        self.private_macros = ""
        self.public_macros = ""
        self.static_functions = ""
        self.static_declarations = ""
        self.module_function_body = ""
        self.struct_decl = f"struct {self.impl_type}\n{{\n"

        self.walk(impl)
        
        m = ""
        m += f"#include \"{file}.h\"\n\n"
        m += self.private_macros
        m += "\n"
        m += self.static_declarations
        m += "\n"
        m += self.static_functions
        m += f"void module_{file}(struct {self.impl_type}* self)\n"
        m += "{\n"
        m += self.module_function_body
        m += "}\n\n"
        
        header = self.impl_type.upper()
        self.struct_decl += "};\n\n"
        h =  f"#ifndef {header}_H\n"
        h += f"#define {header}_H\n"
        h += "#include \"flux.h\"\n"
        for include in self.includes:
            inc = include.lower()
            h += f"#include \"{inc}.h\"\n"
        h += "\n"
        h += self.public_macros
        h += "\n"
        h += self.struct_decl
        h += f"void module_{file}(struct {self.impl_type}* self);\n"
        h += f"#endif /* {header}_H */\n"
        
        path = sys.argv[2]
        m_path = path
        h_path = path.replace(".c",".h")
        
        f = open(m_path,'w')
        f.write(m)
        f.close()

        f = open(h_path,'w')
        f.write(h)
        f.close()

    def eval_func_name(self):
        s = f"eval_{self.eval_name}"
        path = self.get_path()
        depth = self.get_path_depth()
        for idx in path[depth:]:
            s += f"_{idx + 1}"
        return s

    def handle_var_out(self, var):
        var_name = var["name"]
        var_type = var["type"]
        self.eval_name = var_name
        self.set_path_depth()
        self.walk(var)
        expr = self.expr.pop()
        s = f"    self->{var_name} = {expr};\n"
        self.module_function_body += s
        
        self.struct_decl += f"    {var_type} {var_name};\n"
    
    def visit_const(self, var):
        expr = var["expr"]
        const_name = var["name"].upper()
        const_type = var["type"].upper()
        value = expr["val"]
        v = f"#define {const_name} {const_type}({value})\n"
        if var["public"]:
            self.public_macros += v
        else:
            self.private_macros += v

    def visit_in(self, var):
        var_name = var["name"]
        var_type = var["type"]
        self.struct_decl += f"    {var_type} {var_name};\n"

    def visit_var(self, var):
        self.handle_var_out(var)

    def visit_out(self, var):
        self.handle_var_out(var)

    def visit_mod(self, mod):
        mod_name = mod["name"]
        mod_type = mod["type"]
        s = f"    process_{mod_name.lower()}(self);\n"
        self.module_function_body += s
        
        self.mod_name = mod_name
        self.connections = []
        self.walk(mod)
        
        proto = f"static void process_{mod_name}(struct {self.impl_type}* self)"

        s  = f"{proto}\n"
        s +=  "{\n"
        s += f"    struct {mod_type}* {mod_name} = &(self->{mod_name});\n\n"
        for name, expr in self.connections:
            s += f"    {mod_name}->{name} = {expr};\n"
            
        s +=  "\n"
        s += f"    module_{mod_type.lower()}({mod_name});\n"
        s +=  "}\n\n"
        
        self.static_functions += s
        self.static_declarations += f"{proto};\n"
        self.struct_decl += f"    struct {mod_type} {mod_name};\n"

    def visit_con(self, con):
        con_name = con["name"]
        self.eval_name = f"{self.mod_name}_{con_name}"
        self.set_path_depth()
        self.walk(con)
        expr = self.expr.pop()
        self.connections.append((con_name,expr))

    def visit_literal(self, literal):
        self.expr.append(str(literal["val"]))

    def visit_var_ref(self, ref):
        ref_name = ref["name"]
        var = self.scope[ref_name]
        if var["tag"] == "const":
            self.expr.append(ref_name.upper())
        else:
            self.expr.append(f"self->{ref_name}")

    def visit_mod_ref(self, ref):
        module = ref["module"]
        name = ref["name"]
        self.expr.append(f"self->{module}.{name}")

    def visit_op(self, op):
        before_exprs = len(self.expr)
        self.walk(op)
        after_exprs = len(self.expr)

        argv = []
        for _ in range(after_exprs - before_exprs):
            argv.append(self.expr.pop())
        
        op_name = op["name"]
        op_type = op["type"]
        try:
            op_func = op["func"]
        except:
            print(op)
            raise RuntimeError("help")

        if op["nary"]:    
            e = self.eval_func_name()
            self.expr.append(f"{e}(self)")

            arg_type = op["arg_type"]
            proto = f"static {op_type} {e}(struct {self.impl_type}* self)"
            s  = f"{proto}\n"
            s +=  "{\n"
            s += f"    {arg_type} argv[] =\n"
            s +=  "    {\n"
            for arg in reversed(argv):
                s += f"        {arg},\n"
            s +=  "    };\n"
            s +=  "    size_t argc = LEN(argv);\n\n"
            s += f"    return {op_func}(argc, argv);\n"
            s += "}\n\n"
            self.static_functions += s

            s = f"{proto};\n"
            self.static_declarations += s

        else:
            args = ""
            for arg in reversed(argv):
                args += f"{arg},"
            self.expr.append(f"{op_func}({args[:-1]})")