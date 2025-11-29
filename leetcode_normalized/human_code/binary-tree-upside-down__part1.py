class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def upsideDownBinaryTree(self, a1):
        v1, v2, v3 = (a1, None, None)
        while v1:
            v4 = v1.left
            v1.left = v3
            v3 = v1.right
            v1.right = v2
            v2 = v1
            v1 = v4
        return v2
