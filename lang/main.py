import sys
import os.path
from lark import Lark
from parser import Parser
from phases import *
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
grammar = read("lang/sgdl.lark")

parser = Lark(grammar)
tree = parser.parse(src)
# print(tree.pretty())
ast = Parser().transform(tree)
top = {}
top["tag"] = "top"
top["ast"] = ast
top["decls"] = {}
top["impls"] = []

phases = [
    Ban_Decl_Expressions,
    Ban_Input_Expressions,
    Build_Decls,
    Build_Decl_IO,
    Build_Impl_Scope,
    Build_Module_Connections
]

for phase in phases:
    try:
        phase.go(top)
    except GrammarError as e:
        print(e)

print(json.dumps(top,indent=4))
