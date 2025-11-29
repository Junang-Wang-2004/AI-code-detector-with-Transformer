# Time:  O(n)
# Space: O(h)
class NodeRecu(Node):
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
    
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        return NodeRecu.ops[self.val](self.left.evaluate(), self.right.evaluate())
        

class TreeBuilder2(object):
    def buildTree(self, postfix):
        """
        """
        stk = []
        for c in postfix:
            if c.isdigit():
                stk.append(NodeRecu(c))
            else:
                node = NodeRecu(c)
                node.right = stk.pop()
                node.left = stk.pop()
                stk.append(node)
        return stk.pop()
