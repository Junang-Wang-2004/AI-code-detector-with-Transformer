class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxAncestorDiff(self, a1):
        v1 = 0
        v2 = [(a1, a1.val, a1.val)] if a1 else []
        while v2:
            v3, v4, v5 = v2.pop()
            v6 = v4 - v3.val
            v7 = v3.val - v5
            v1 = max(v1, v6, v7)
            v8 = max(v4, v3.val)
            v9 = min(v5, v3.val)
            if v3.left:
                v2.append((v3.left, v8, v9))
            if v3.right:
                v2.append((v3.right, v8, v9))
        return v1
