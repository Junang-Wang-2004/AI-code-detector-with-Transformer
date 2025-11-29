class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def upsideDownBinaryTree(self, a1):
        v1 = None
        v2 = None
        v3 = a1
        while v3:
            v4 = v3.left
            v5 = v3.right
            v3.left = v2
            v3.right = v1
            v2 = v5
            v1 = v3
            v3 = v4
        return v1
