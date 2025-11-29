class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isValidBST(self, a1):
        v1, v2 = (None, a1)
        while v2:
            if v2.left is None:
                if v1 and v1.val >= v2.val:
                    return False
                v1 = v2
                v2 = v2.right
            else:
                v3 = v2.left
                while v3.right and v3.right != v2:
                    v3 = v3.right
                if v3.right is None:
                    v3.right = v2
                    v2 = v2.left
                else:
                    if v1 and v1.val >= v2.val:
                        return False
                    v3.right = None
                    v1 = v2
                    v2 = v2.right
        return True
