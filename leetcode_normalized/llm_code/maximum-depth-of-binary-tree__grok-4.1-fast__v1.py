class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def maxDepth(self, a1):
        if not a1:
            return 0
        v1 = [(a1, 1)]
        v2 = 0
        while v1:
            v3, v4 = v1.pop()
            v2 = max(v2, v4)
            if v3.right:
                v1.append((v3.right, v4 + 1))
            if v3.left:
                v1.append((v3.left, v4 + 1))
        return v2
