class C1(Node):
    v1 = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        return C1.ops[self.val](self.left.evaluate(), self.right.evaluate())

class C2(object):

    def buildTree(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2.isdigit():
                v1.append(C1(v2))
            else:
                v3 = C1(v2)
                v3.right = v1.pop()
                v3.left = v1.pop()
                v1.append(v3)
        return v1.pop()
