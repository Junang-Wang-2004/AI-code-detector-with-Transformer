class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def postorderTraversal(self, a1):
        """
        """
        v1 = C1(0)
        v1.left = a1
        v2, v3 = ([], v1)
        while v3:
            if v3.left is None:
                v3 = v3.right
            else:
                v4 = v3.left
                while v4.right and v4.right != v3:
                    v4 = v4.right
                if v4.right is None:
                    v4.right = v3
                    v3 = v3.left
                else:
                    v2 += self.traceBack(v3.left, v4)
                    v4.right = None
                    v3 = v3.right
        return v2

    def traceBack(self, a1, a2):
        v1, v2 = ([], a1)
        while v2 is not a2:
            v1.append(v2.val)
            v2 = v2.right
        v1.append(a2.val)
        v1.reverse()
        return v1
