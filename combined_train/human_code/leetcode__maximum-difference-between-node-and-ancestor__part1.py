class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxAncestorDiff(self, a1):
        """
        """
        v1 = 0
        v2 = [(a1, 0, float('inf'))]
        while v2:
            v3, v4, v5 = v2.pop()
            if not v3:
                continue
            v1 = max(v1, v4 - v3.val, v3.val - v5)
            v4 = max(v4, v3.val)
            v5 = min(v5, v3.val)
            v2.append((v3.left, v4, v5))
            v2.append((v3.right, v4, v5))
        return v1
