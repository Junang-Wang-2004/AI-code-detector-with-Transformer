class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def insertIntoBST(self, a1, a2):
        if a1 is None:
            return C1(a2)
        v1 = a1
        while True:
            if a2 <= v1.val:
                if v1.left is None:
                    v1.left = C1(a2)
                    return a1
                v1 = v1.left
            else:
                if v1.right is None:
                    v1.right = C1(a2)
                    return a1
                v1 = v1.right
