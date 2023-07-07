
class Walker:
    def visit(self,parent,child): pass
    
    def walk(self,node):
        p = (len(self.parent) == 0) or (node["tag"] in self.parent)
        for key,val in node.items():
            if key[0] == "_": continue
            if (node["tag"] == "top") and (key == "decls"): continue
            if (node["tag"] == "top") and (key == "impls"): continue

            if isinstance(val,dict):
                c = (len(self.child) == 0) or (val["tag"] in self.child)
                if p and c: self.visit(node,val)
                self.walk(val)
            elif isinstance(val,list):
                for item in val:
                    if isinstance(item,dict):
                        c = (len(self.child) == 0) or (item["tag"] in self.child)
                        if p and c: self.visit(node,item)
                        self.walk(item)
