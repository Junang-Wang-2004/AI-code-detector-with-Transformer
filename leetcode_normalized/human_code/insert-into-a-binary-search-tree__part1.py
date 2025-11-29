class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def insertIntoBST(self, a1, a2):
        """
        """
        v1, v2 = (a1, None)
        while v1:
            v2 = v1
            if a2 <= v1.val:
                v1 = v1.left
            else:
                v1 = v1.right
        if not v2:
            a1 = C1(a2)
        elif a2 <= v2.val:
            v2.left = C1(a2)
        else:
            v2.right = C1(a2)
        return a1
