import sys
import os.path
from lark import Lark
from parser import Parser
from phases import *
from c_repr import *
import json

def read(path):
    f = open(path,'r')
    s = f.read()
    f.close()
    return s

def write(path,s):
    f = open(path,'w')
    f.write(s)
    f.close()

src = read(sys.argv[1])
grammar = read("lang/flux.lark")

parser = Lark(grammar)
tree = parser.parse(src)
# print(tree.pretty())
ast = Parser().transform(tree)
top = {}
top["tag"] = "top"
top["ast"] = ast

phases = [
    Build_Decl_Scope,
    Build_Impl_Scope,
    Validate_References,
    Infer_Op_Types,
    Emit_C_Repr
]

for phase in phases:
    try:
        phase.go(top)
    except GrammarError as e:
        print(e)
        break

# print(json.dumps(top,indent=4))
