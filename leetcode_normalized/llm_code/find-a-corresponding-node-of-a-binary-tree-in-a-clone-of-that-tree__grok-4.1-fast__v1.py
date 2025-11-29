class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def getTargetCopy(self, a1, a2, a3):

        def traverse(a1, a2):
            if a1 is None:
                return None
            if a1 == a3:
                return a2
            v1 = traverse(a1.left, a2.left)
            if v1 is not None:
                return v1
            return traverse(a1.right, a2.right)
        return traverse(a1, a2)
