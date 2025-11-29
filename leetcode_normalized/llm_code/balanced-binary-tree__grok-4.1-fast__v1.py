class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isBalanced(self, a1):

        def validate(a1):
            if not a1:
                return (True, 0)
            v1, v2 = validate(a1.left)
            v3, v4 = validate(a1.right)
            if not v1 or not v3:
                return (False, 0)
            v5 = abs(v2 - v4)
            v6 = v5 <= 1
            v7 = max(v2, v4) + 1
            return (v6, v7)
        v1, v2 = validate(a1)
        return v1
