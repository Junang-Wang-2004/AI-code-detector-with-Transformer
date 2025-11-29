class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def preorderTraversal(self, a1):
        """
        """
        v1, v2 = ([], a1)
        while v2:
            if v2.left is None:
                v1.append(v2.val)
                v2 = v2.right
            else:
                v3 = v2.left
                while v3.right and v3.right != v2:
                    v3 = v3.right
                if v3.right is None:
                    v1.append(v2.val)
                    v3.right = v2
                    v2 = v2.left
                else:
                    v3.right = None
                    v2 = v2.right
        return v1
