class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def sufficientSubset(self, a1, a2):

        def has_path(a1, a2):
            if a1 is None:
                return False
            if a1.left is None and a1.right is None:
                return a1.val >= a2
            v1 = has_path(a1.left, a2 - a1.val)
            v2 = has_path(a1.right, a2 - a1.val)
            if not v1:
                a1.left = None
            if not v2:
                a1.right = None
            return v1 or v2
        if has_path(a1, a2):
            return a1
        return None
