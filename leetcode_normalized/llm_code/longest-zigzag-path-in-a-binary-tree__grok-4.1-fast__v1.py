class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def longestZigZag(self, a1):
        self.best = 0

        def explore(a1):
            if a1 is None:
                return (-1, -1)
            v1, v2 = explore(a1.left)
            v3, v4 = explore(a1.right)
            v5 = 1 + v2
            v6 = 1 + v3
            self.best = max(self.best, v5, v6)
            return (v5, v6)
        explore(a1)
        return self.best
