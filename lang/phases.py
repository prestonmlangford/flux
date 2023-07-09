from walk import Walker

class GrammarError(Exception): pass

def none(thing): return thing is None
def some(thing): return not none(thing)

class Build_Decl_Scope(Walker):
    def go(top):
        w = Build_Decl_Scope()
        w.decls = {}
        w.consts = {}
        top["_decls"] = w.decls
        top["_consts"] = w.consts
        w.walk(top)

    def visit_decl(self,decl):
        self.decl_name = decl["type"]
        self.ins = {}
        self.outs = {}
        decl["_ins"] = self.ins
        decl["_outs"] = self.outs
        self.decls[self.decl_name] = decl
        self.walk(decl)

    def visit_impl(self,impl):
        # do not visit impls in this phase
        pass

    def visit_in(self,var):
        if some(var["expr"]):
            raise GrammarError("Expressions are not allowed for module declarations")
        name = var["name"]
        self.ins[name] = var

    def visit_out(self,var):
        if some(var["expr"]):
            raise GrammarError("Expressions are not allowed for module declarations")
        name = var["name"]
        self.outs[name] = var

    def visit_const(self,var):
        if some(var["expr"]):
            raise GrammarError("Expressions are not allowed for module declarations")
        const_name = var["name"]
        name = f"{self.decl_name}::{const_name}"
        self.consts[name] = var

class Build_Impl_Scope(Walker):
    def go(top):
        w = Build_Impl_Scope()
        w.decls = top["_decls"]
        w.consts = top["_consts"]
        w.walk(top)

    def visit_decl(self, node):
        # do not visit decls in this phase
        pass

    def visit_impl(self, impl):
        self.mod_type = impl["type"]
        self.scope = {}
        impl["_scope"] = self.scope
        self.walk(impl)

    def visit_in(self, var):
        name = var["name"]
        self.scope[name] = var

    def visit_var(self, var):
        name = var["name"]
        self.scope[name] = var

    def visit_const(self, var):
        name = var["name"]
        key = f"{self.mod_type}::{name}"
        var["public"] = key in self.consts
        self.scope[key] = var

    def visit_mod(self, mod):
        self.mod_type = mod["type"]
        mod_name = mod["name"]

        try:
            self.mod_decl = self.decls[self.mod_type]
        except:
            raise GrammarError(f"No declaration for module {self.mod_type}")

        for key,val in self.mod_decl["_outs"].items():
            name = f"{mod_name}.{key}"
            self.scope[name] = val

        self.walk(mod)

    def visit_con(self, con):
        con_name = con["name"]
        
        try:
            var = self.mod_decl["_ins"][con_name]
        except:
            raise GrammarError(f"{con_name} is not an input to module {self.mod_type}")

        con["type"] = var["type"]
        con["size"] = var["size"]

class Validate_References(Walker):
    def go(top):
        w = Validate_References()
        w.public_consts = top["_consts"]
        w.walk(top)

    def visit_decl(self, node):
        # do not visit decls in this phase
        pass

    def visit_impl(self, impl):
        self.mod_type = impl["type"]
        self.scope = impl["_scope"]
        self.walk(impl)

    def visit_var_ref(self, ref):
        name = ref["name"]

        try:
            var = self.scope[name]
        except:
            raise GrammarError(f"Undeclared reference to {name}")

        ref["type"] = var["type"]
        ref["size"] = var["size"]

    def visit_mod_ref(self, ref):
        module = ref["module"]
        name = ref["name"]
        key = f"{module}.{name}"

        try:
            var = self.scope[key]
        except:
            raise GrammarError(f"Undeclared reference to {key}")

        ref["type"] = var["type"]
        ref["size"] = var["size"]

    def visit_const_ref(self, ref):
        module = ref["module"]
        if module == "this":
            module = self.mod_type
            ref["module"] = module

        name = ref["name"]
        key = f"{module}::{name}"

        try:
            var = self.scope[key]
        except:
            try:
                var = self.public_consts[key]
            except:
                raise GrammarError(f"Undeclared reference to {key}")

        ref["type"] = var["type"]
        ref["size"] = var["size"]


class Infer_Op_Types(Walker):
    """
    f: floating point number
    s: signed integer
    u: unsigned integer
    b: boolean

    sum(fsu...) -> fsu
    sub(fsu,fsu) -> fsu
    mul(fsu...) -> fsu
    div(fsu,fsu) -> fsu
    rem(su,su) -> su
    neg(fsu) -> fsu
    and(bu...) -> bu
    nand(bu...) -> bu
    or(bu...) -> bu
    nor(bu...) -> bu
    xor(bu...) -> bu
    xnor(bu...) -> bu
    not(bu) -> bu
    eq(su...) -> b
    neq(su...) -> b
    gt(fsu,fsu) -> b
    gte(su,su) -> b
    lt(fsu,fsu) -> b
    lte(su,su) -> b
    
    -------------------
    # n-ary
    sum(fsu...) -> fsu
    mul(fsu...) -> fsu
    and(bu...) -> bu
    nand(bu...) -> bu
    or(bu...) -> bu
    nor(bu...) -> bu
    xor(bu...) -> bu
    xnor(bu...) -> bu

    # binary
    sub(fsu,fsu) -> fsu
    div(fsu,fsu) -> fsu
    rem(su,su) -> su

    # unary
    neg(fsu) -> fsu
    not(bu) -> bu

    # n-ary bool
    eq(su...) -> b
    neq(su...) -> b

    # binary bool
    gt(fsu,fsu) -> b
    gte(su,su) -> b
    lt(fsu,fsu) -> b
    lte(su,su) -> b
    """

    F = set(["f32","f64"])
    S = set(["i8","i16","i32","i64"])
    U = set(["u8","u16","u32","u64"])
    B = set(["boolean"])
    
    FSU = F | S | U
    SU = S | U
    BU = B | U

    def go(top):
        w = Infer_Op_Types()
        w.walk(top)

    def nary(self, op, types):
        args = op["args"]
        op_type = args[0]["type"]
        if not (op_type in types):
            raise GrammarError(f"Invalid type {op_type}")

        for arg in args:
            _op_type = arg["type"]
            if op_type != _op_type:
                raise GrammarError(f"Mismatched types ({op_type} and {_op_type}) in op sum")

        op["type"] = op_type
        op["arg_type"] = op_type
        op["nary"] = True

    def binary(self, op, types):
        args = op["args"]
        if len(args) != 2:
            raise GrammarError(f"Need at least two arguments")

        x_type = args[0]["type"]
        y_type = args[1]["type"]
        if not (x_type in types):
            raise GrammarError(f"Invalid type {x_type}")

        if x_type != y_type:
            raise GrammarError(f"Mismatched types ({x_type} and {y_type}) in op sum")

        op["type"] = x_type
        op["arg_type"] = x_type
        op["nary"] = False

    def unary(self, op, types):
        args = op["args"]
        if len(args) != 1:
            raise GrammarError(f"Only one argument allowed")

        op_type = args[0]["type"]
        if not (op_type in types):
            raise GrammarError(f"Invalid type {op_type}")

        op["type"] = op_type
        op["arg_type"] = op_type
        op["nary"] = False

    def nary_bool(self, op, types):
        args = op["args"]
        arg_type = args[0]["type"]
        if not (arg_type in types):
            raise GrammarError(f"Invalid type {arg_type}")

        for arg in args:
            _arg_type = arg["type"]
            if arg_type != _arg_type:
                raise GrammarError(f"Mismatched types ({arg_type} and {_arg_type})")

        op["type"] = "boolean"
        op["arg_type"] = arg_type
        op["nary"] = True

    def binary_bool(self, op, types):
        args = op["args"]
        arg_type = args[0]["type"]
        if not (arg_type in types):
            raise GrammarError(f"Invalid type {arg_type}")

        for arg in args:
            _arg_type = arg["type"]
            if arg_type != _arg_type:
                raise GrammarError(f"Mismatched types ({arg_type} and {_arg_type})")
        
        op["type"] = "boolean"
        op["arg_type"] = arg_type
        op["nary"] = False


    def visit_sum(self, op):
        self.nary(op, self.FSU)
        
    def visit_sub(self, op):
        self.binary(op, self.FSU)
        
    def visit_mul(self, op):
        self.nary(op, self.FSU)
        
    def visit_div(self, op):
        self.binary(op, self.FSU)
        
    def visit_rem(self, op):
        self.binary(op, self.SU)
        
    def visit_neg(self, op):
        self.unary(op, self.FSU)
        
    def visit_and(self, op):
        self.nary(op, self.BU)
        
    def visit_nand(self, op):
        self.nary(op, self.BU)
        
    def visit_or(self, op):
        self.nary(op, self.BU)
        
    def visit_nor(self, op):
        self.nary(op, self.BU)
        
    def visit_xor(self, op):
        self.nary(op, self.BU)
        
    def visit_xnor(self, op):
        self.nary(op, self.BU)
        
    def visit_not(self, op):
        self.unary(op, self.BU)
        
    def visit_eq(self, op):
        self.nary_bool(op, self.SU)
        
    def visit_neq(self, op):
        self.nary_bool(op, self.SU)
        
    def visit_gt(self, op):
        self.binary_bool(op, self.FSU)
        
    def visit_gte(self, op):
        self.binary_bool(op, self.SU)
        
    def visit_lt(self, op):
        self.binary_bool(op, self.FSU)
        
    def visit_lte(self, op):
        self.binary_bool(op, self.SU)

    def visit_cast(self,op):
        op["type"] = "PMLFIXME"
        op["arg_type"] = "PMLFIXME"
        op["nary"] = False

    def visit_op(self,op):

        # deal with nested expressions first
        self.walk(op)

        # call correct handler
        op_name = op["name"]
        visitor = getattr(self,f"visit_{op_name}")
        visitor(op)
