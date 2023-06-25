from lark import Transformer

class Parser(Transformer):
    def r_tag_in(self,_):
        return "in"

    def r_tag_out(self,_):
        return "out"

    def r_tag_var(self,_):
        return "var"

    def r_tag_block(self,_):
        return "block"

    def r_tag_module(self,_):
        return "module"

    def r_var_size(self,items):
        try:
            return int(items[0])
        except:
            return None

    def r_var_expr(self,items):
        try:
            return items[0]
        except:
            return None

    def r_op_args(self,items):
        return items
    
    def r_op(self,items):
        return {
            "tag"  : "op",
            "name" : str(items[0]),
            "args" : items[1]
        }

    def r_constant(self, items):
        return {
            "tag"  : "const",
            "type" : str(items[0]),
            "val"  : int(items[1])
        }

    def r_reference(self,items):
        return {
            "tag"  : "ref",
            "path" : list(map(str,items))
        }

    def r_var(self, items):
        return {
            "tag"  : items[0],
            "type" : str(items[1]),
            "name" : str(items[2]),
            "size" : items[3],
            "expr" : items[4]
        }
        
    def r_state_decl_items(self,items):
        return items

    def r_state_decl(self,items):
        return {
            "tag"   : items[0],
            "type"  : str(items[1]),
            "vars"  : items[2]
        }

    def r_state_connection(self,items):
        return {
            "tag"  : "connect",
            "name" : str(items[0]),
            "expr" : items[1]
        }

    def r_state_expr(self,items):
        return items

    def r_state(self,items):
        return {
            "tag"  : items[0],
            "type" : str(items[1]),
            "name" : str(items[2]),
            "cons" : items[3]
        }

    def start(self,items):
        return items
