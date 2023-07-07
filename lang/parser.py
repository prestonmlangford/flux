from lark import Transformer

class Parser(Transformer):
    def r_tag_in(self,_):
        return "in"

    def r_tag_out(self,_):
        return "out"

    def r_tag_var(self,_):
        return "var"

    def r_tag_const(self,_):
        return "const"

    def r_tag_mod(self,_):
        return "mod"

    def r_tag_decl(self,_):
        return "decl"

    def r_tag_impl(self,_):
        return "impl"

    def r_literal(self, items):
        return {
            "tag"  : "literal",
            "type" : str(items[0]),
            "val"  : int(items[1])
        }

    def r_mod_reference(self,items):
        return {
            "tag"  : "mod_ref",
            "module" : str(items[0]),
            "output" : str(items[1])
        }


    def r_var_reference(self,items):
        return {
            "tag"  : "var_ref",
            "name" : str(items[0])
        }

    def r_namespace(self,items):
        return {
            "tag"  : "namespace",
            "mod" : str(items[0]),
            "name" : str(items[1])
        }

    def r_op_args(self,items):
        return items

    def r_op(self,items):
        try:
            args = items[1]
        except:
            args = None

        return {
            "tag"  : "op",
            "name" : str(items[0]),
            "args" : args
        }

    def r_val_size(self,items):
        try:
            return int(items[0])
        except:
            return None

    def r_val_expr(self,items):
        try:
            return items[0]
        except:
            return None

    def r_val(self, items):
        return {
            "tag"  : items[0],
            "type" : str(items[1]),
            "name" : str(items[2]),
            "size" : items[3],
            "expr" : items[4]
        }

    def r_mod_connection(self,items):
        return {
            "tag"  : "connect",
            "name" : str(items[0]),
            "expr" : items[1]
        }

    def r_mod_connections(self,items):
        return items

    def r_mod(self,items):
        return {
            "tag"  : items[0],
            "type" : str(items[1]),
            "name" : str(items[2]),
            "cons" : items[3]
        }

    def r_mod_decl_items(self,items):
        return items

    def r_mod_decl(self,items):
        return {
            "tag"   : items[0],
            "type"  : str(items[1]),
            "vars"  : items[2]
        }

    def start(self,items):
        return items
