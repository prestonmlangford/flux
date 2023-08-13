import os
import importlib

"""
f: floating point number
i: signed integer
u: unsigned integer
b: boolean

and(bu...) -> bu
div(fiu,fiu) -> fiu
eq(iu...) -> b
gt(fiu,fiu) -> b
gte(iu,iu) -> b
lt(fiu,fiu) -> b
lte(iu,iu) -> b
mul(fiu...) -> fiu
nand(bu...) -> bu
neg(fi) -> fi
neq(iu...) -> b
nor(bu...) -> bu
not(bu) -> bu
or(bu...) -> bu
rem(iu,iu) -> iu
sub(fiu,fiu) -> fiu
sum(fiu...) -> fiu
xnor(bu...) -> bu
xor(bu...) -> bu

"""

def write(name,s):
    here = os.getcwd()
    path = os.path.join(here, f"../lib/ops/{name}")
    f = open(path,'w')
    f.write(s)
    f.close()

def gen(module,name):
    h_macro = name.upper()
    h = name.lower()

    decl = ""
    decl += f"#ifndef {h_macro}_H\n"
    decl += f"#define {h_macro}_H\n"

    impl = ""
    impl += f"#include \"flux.h\"\n"
    impl += f"#include \"{h}.h\"\n"
    
    for i in range(4):
        width = 1 << (i + 3)

        impl += module.impl_u.replace("$",str(width))
        impl += module.impl_i.replace("$",str(width))
        impl += module.impl_f.replace("$",str(width))

        decl += module.decl_u.replace("$",str(width))
        decl += module.decl_i.replace("$",str(width))
        decl += module.decl_f.replace("$",str(width))

    for i in range(2):
        width = 1 << (i + 5)
        impl += module.impl_f.replace("$",str(width))
        decl += module.decl_f.replace("$",str(width))
    
    impl += module.impl_b.replace("$",str(width))
    decl += module.decl_b.replace("$",str(width))
        
    

    decl += f"\n#endif /* {h_macro}_H */\n"
    
    
    write(f"{h}.c",impl)
    write(f"{h}.h",decl)
    

for file in os.listdir("oplib"):
    if file[0] == "_": continue
    if not (".py" in file): continue
    
    name = file.replace('.py','')
    path = f"oplib.{name}"
    module = importlib.import_module(path)
    
    gen(module,name)
    
    print(f"#include \"ops/{name}.h\"")
    