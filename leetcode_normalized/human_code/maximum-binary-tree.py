class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def constructMaximumBinaryTree(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            v3 = C1(v2)
            while v1 and v2 > v1[-1].val:
                v3.left = v1.pop()
            if v1:
                v1[-1].right = v3
            v1.append(v3)
        return v1[0]
