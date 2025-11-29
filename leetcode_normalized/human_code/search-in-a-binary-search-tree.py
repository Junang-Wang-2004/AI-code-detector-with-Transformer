class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def searchBST(self, a1, a2):
        """
        """
        while a1 and a2 != a1.val:
            if a2 < a1.val:
                a1 = a1.left
            else:
                a1 = a1.right
        return a1
