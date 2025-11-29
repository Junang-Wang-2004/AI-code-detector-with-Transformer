class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def isSymmetric(self, a1):

        def helper(a1, a2):
            if not a1 or not a2:
                return a1 == a2
            return a1.val == a2.val and helper(a1.left, a2.right) and helper(a1.right, a2.left)
        return bool(a1) == False or helper(a1.left, a1.right)
