from lark import Lark
from lark.visitors import Visitor_Recursive as Visitor
from lark import Transformer

def none(thing): return thing is None
def some(thing): return not none(thing)

def show(items):
    lst = []
    for item in items:
        lst.append(f"{type(item).__name__}({item})")
    print(", ".join(lst))

class Constant:
    def __init__(self,type,val) -> None:
        self.type = type
        self.val = val

    def __repr__(self) -> str:
        return f"{self.type}({self.val})"
    
    def process_repr(self) -> str:
        if self.type == "bool":
            return "true" if self.val == 1 else "false"
        else:
            post = ""

            if "u" in self.type:
                post = "U"

            if "64" in self.type:
                post += "LL"

            return f"{self.val}{post}"

class Reference:
    def __init__(self,ids) -> None:
        self.ids = ids

    def __repr__(self) -> str:
        return ".".join(self.ids)
    
    def process_repr(self) -> str:
        return f"self->{self}"
    
class Variable:
    def __init__(self,tag,type,name,size,expr) -> None:
        self.tag  = tag
        self.type  = type
        self.name = name
        self.size = size
        self.expr = expr
        
        if (self.tag == "in") and some(self.expr):
            raise RuntimeError("input declarations can not be connected")
    
    def __repr__(self) -> str:
        s = f"{self.tag} {self.type} {self.name}"
        if self.size:
            s += f"[{self.size}]"
        if self.expr:
            s += f" = {self.expr}"
        s += ";"
        return s

class Op:
    def __init__(self,name,args) -> None:
        self.name = name
        self.args = args
    
    def __repr__(self) -> str:
        lst = []
        for arg in self.args:
            lst.append(f"{arg}")
        fargs = ",".join(lst)
        return f"{self.name}({fargs})"

class StateDecl:
    def __init__(self,tag,type,variables) -> None:
        self.tag  = tag
        self.type  = type
        self.variables = variables

    def __repr__(self) -> str:
        s = f"{self.tag} {self.type}"
        s += " {" 
        for var in self.variables:
            s += f"{var}"
        s += "};"
        return s

class Connection:
    def __init__(self,name,expr) -> None:
        self.name = name
        self.expr = expr
    
    def __repr__(self) -> str:
        return f".{self.name} = {self.expr}"
    
    
class StateInst:
    def __init__(self,tag,type,name,connections) -> None:
        self.tag = tag
        self.type = type
        self.name = name
        self.connections = connections
    
    def __repr__(self) -> str:
        s = f"{self.tag} {self.type} {self.name} {{"
        for connection in self.connections:
            s += f"{connection},"
        s = s[:-1] + "};"
        return s

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
        name, args = items
        return Op(name,args)

    def r_constant(self, items):
        t,v = items
        return Constant(str(t),int(v))

    def r_reference(self,items):
        return Reference(list(map(str,items)))

    def r_var(self, items):
        tag, type, name, size, expr = items
        return Variable(tag, type, name, size, expr)

    def r_state_decl_items(self,items):
        return items

    def r_state_decl(self,items):
        tag, type, things = items
        return StateDecl(tag,type,things)

    def r_state_connection(self,items):
        name, expr = items
        return Connection(name,expr)

    def r_state_expr(self,items):
        return items

    def r_state(self,items):
        tag, type, name, connections = items
        return StateInst(tag,type,name,connections)

    def start(self,items):
        return items

def write_process_funcs(module: StateDecl):
    for var in module.variables:
        if var.tag == "in":
            continue
        elif (var.tag == "module") or (var.tag == "block"):
            s = f"static void process_{var.name}(struct {module.type}* self)\n"
            s += "{\n"
            s += f"    struct {var.type}* {var.name} = &(self->{var.name});\n\n"
            for connection in var.connections:
                name = connection.name
                expr = connection.expr.process_repr()
                s += f"    {var.name}->{name} = {expr};\n"
            
            s += "\n"
            s += f"    {var.tag}_{var.type}({var.name});\n"
            s += "}\n\n"
            print(s)
