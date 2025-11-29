class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def hasPathSum(self, a1, a2):
        if not a1:
            return False
        v1 = [(a1, a1.val)]
        while v1:
            v2, v3 = v1.pop()
            if not v2.left and (not v2.right):
                if v3 == a2:
                    return True
            if v2.right:
                v1.append((v2.right, v3 + v2.right.val))
            if v2.left:
                v1.append((v2.left, v3 + v2.left.val))
        return False
