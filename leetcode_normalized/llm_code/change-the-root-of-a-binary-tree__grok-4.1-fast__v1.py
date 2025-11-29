class C1:

    def __init__(self, a1):
        pass

class C2(object):

    def flipBinaryTree(self, a1, a2):
        v1 = None
        v2 = a2
        while v2 != a1:
            v3 = v2.parent
            v2.parent = v1
            if v2.left == v1:
                v2.left = None
            elif v2.right == v1:
                v2.right = None
            if v2.left:
                v2.right = v2.left
            v2.left = v3
            v1 = v2
            v2 = v3
        a1.parent = v1
        if a1.left == v1:
            a1.left = None
        elif a1.right == v1:
            a1.right = None
        return a2
