from lark import Lark
from dparse import Parser
from emit import *

f = open("landing.vs",'r')
src = f.read()
f.close()

f = open("grammar.lark",'r')
grammer = f.read()
f.close()

parser = Lark(grammer)
tree = parser.parse(src)
decls = Parser().transform(tree)

for decl in decls:
    if decl["tag"] == "module":
        print(c_repr_process_func(decl))
        print(c_repr_module_func(decl))
        print(c_repr_module_struct(decl))