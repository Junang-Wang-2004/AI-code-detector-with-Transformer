class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def correctBinaryTree(self, a1):
        """
        """
        v1 = {a1: None}
        while v1:
            v2 = {}
            for v3, v4 in v1.items():
                if v3.right in v1:
                    if v4.left == v3:
                        v4.left = None
                    else:
                        v4.right = None
                    return a1
                if v3.left:
                    v2[v3.left] = v3
                if v3.right:
                    v2[v3.right] = v3
            v1 = v2
