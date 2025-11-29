class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def searchBST(self, a1, a2):
        if a1 is None or a1.val == a2:
            return a1
        if a2 < a1.val:
            return self.searchBST(a1.left, a2)
        return self.searchBST(a1.right, a2)
