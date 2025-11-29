class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def distributeCoins(self, a1):

        def traverse(a1):
            if not a1:
                return (0, 0)
            v1, v2 = traverse(a1.left)
            v3, v4 = traverse(a1.right)
            v5 = abs(v1) + abs(v3)
            v6 = v2 + v4 + v5
            v7 = a1.val + v1 + v3 - 1
            return (v7, v6)
        v1, v2 = traverse(a1)
        return v2
