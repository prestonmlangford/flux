from walk import Walker

class Emit_C_Repr(Walker):
    def go(top):
        w = Emit_C_Repr()

        w.eval_name = ""
        w.expr = []

        w.walk(top)
    
    def set_path_depth(self):
        self.path_depth = len(self.get_path())
    
    def get_path_depth(self):
        return self.path_depth
    
    def pop_expr(self):
        return self.expr.pop()

    def push_expr(self, expr):
        self.expr.append(expr)
    
    def visit_decl(self, node):
        # decl info only used to verify grammar rules are met
        pass

    def visit_impl(self, impl):
        self.impl_type = impl["type"]
        header = self.impl_type.upper()
        file = self.impl_type.lower()

        self.static_functions = ""
        self.static_declarations = ""
        self.module_function_body = ""
        self.struct_decl = f"struct {self.impl_type}\n{{\n"
        self.walk(impl)
        
        m = ""
        m += f"void module_{file}(struct {self.impl_type}* self)\n"
        m += "{\n"
        m += self.module_function_body
        m += "}\n\n"
        
        header = self.impl_type.upper()
        self.struct_decl += "};\n\n"
        h =  f"#ifndef {header}_H\n"
        h += f"#define {header}_H\n"
        h += "#include \"types.h\"\n\n"
        h += self.struct_decl
        h += f"#endif /* {header}_H */\n"
        
        f = open(f"out/{file}.c",'w')
        f.write(f"#include \"{file}.h\"\n")
        f.write(f"#include \"ops.h\"\n\n")
        f.write(self.static_declarations + "\n")
        f.write(self.static_functions)
        f.write(m)
        f.close()

        f = open(f"out/{file}.h",'w')
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
        expr = self.pop_expr()
        s = f"    self->{var_name} = {expr};\n"
        self.module_function_body += s
        
        self.struct_decl += f"    {var_type} {var_name};\n"

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
        expr = self.pop_expr()
        self.connections.append((con_name,expr))

    def visit_literal(self, literal):
        self.push_expr(str(literal["val"]))

    def visit_ref(self, ref):
        name = ref["name"]
        if "::" in name:
            self.push_expr(f"PMLFXIME {name}")
        else:
            self.push_expr(f"self->{name}")

    def visit_op(self, op):
        before = len(self.expr)
        self.walk(op)
        after = len(self.expr)

        argv = []
        for _ in range(after - before):
            argv.append(self.expr.pop())
        
        op_name = op["name"]
        op_type = op["type"]
        op_func = f"{op_type}_{op_name}"

        if op["nary"]:    
            e = self.eval_func_name()
            self.push_expr(f"{e}(self)")

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
            self.push_expr(f"{op_func}({args[:-1]})")