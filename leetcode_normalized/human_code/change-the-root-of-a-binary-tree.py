class C1:

    def __init__(self, a1):
        pass

class C2(object):

    def flipBinaryTree(self, a1, a2):
        """
        """
        v1, v2 = (a2, None)
        while True:
            v3 = v1.parent
            v1.parent = v2
            if v1.left == v2:
                v1.left = None
            else:
                v1.right = None
            if v1 == a1:
                break
            if v1.left:
                v1.right = v1.left
            v1.left = v3
            v1, v2 = (v3, v1)
        return a2
