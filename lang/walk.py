"""
class Walker:
    def visit(self,node):
        tag = node["tag"]
        v = f"visit_{tag}"
        try:
            visitor = getattr(self,v)
            visitor(self,node)
        except:
            pass

    def walk(self,node):
        for key,val in node.items():
            if key[0] == "_": continue
            
            if isinstance(val,dict):
                self.visit(val)
                self.walk(val)
            elif isinstance(val,list):
                for item in val:
                    if isinstance(item,dict):
                        self.visit(item)
                        self.walk(item)
"""

class Walker(object):
    """ A base NodeVisitor class for visiting c_ast nodes.
        Subclass it and define your own visit_XXX methods, where
        XXX is the class name you want to visit with these
        methods.

        For example:

        class ConstantVisitor(NodeVisitor):
            def __init__(self):
                self.values = []

            def visit_Constant(self, node):
                self.values.append(node.value)

        Creates a list of values of all the constant nodes
        encountered below the given node. To use it:

        cv = ConstantVisitor()
        cv.visit(node)

        Notes:

        *   generic_visit() will be called for AST nodes for which
            no visit_XXX method was defined.
        *   The children of nodes for which a visit_XXX was
            defined will not be visited - if you need this, call
            walk() on the node.
            You can use:
                self.walk(node)
        *   Modeled after Python's own AST visiting facilities
            (the ast module of Python 3.0)
    """

    

    def __init__(self) -> None:
        self._method_cache = None
        self.walk_path = []
    
    def get_path(self):
        return self.walk_path

    def push_path(self):
        self.walk_path.append(0)
    
    def inc_path(self):
        idx = len(self.walk_path) - 1
        self.walk_path[idx] += 1
        
    def pop_path(self):
        return self.walk_path.pop()

    def visit(self, node):
        """ Visit a node.
        """

        if self._method_cache is None:
            self._method_cache = {}
        
        tag = node["tag"]

        visitor = self._method_cache.get(tag, None)
        if visitor is None:
            method = f"visit_{tag}"
            visitor = getattr(self, method, self.walk)
            self._method_cache[tag] = visitor

        return visitor(node)

    def walk(self, node):
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        for key,val in node.items():
            if key[0] == "_":
                # not part of the graph
                pass

            elif isinstance(val,dict):
                self.visit(val)
            
            elif isinstance(val,list):
                self.push_path()
                for item in val:
                    if isinstance(item,dict):
                        self.visit(item)
                        self.inc_path()
                self.pop_path()
