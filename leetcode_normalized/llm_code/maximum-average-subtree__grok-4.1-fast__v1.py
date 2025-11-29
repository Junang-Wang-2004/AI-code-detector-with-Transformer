class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maximumAverageSubtree(self, a1):
        self.max_avg = 0.0

        def traverse(a1):
            if not a1:
                return (0, 0)
            v1, v2 = traverse(a1.left)
            v3, v4 = traverse(a1.right)
            v5 = v1 + v3 + a1.val
            v6 = v2 + v4 + 1
            self.max_avg = max(self.max_avg, v5 / v6)
            return (v5, v6)
        traverse(a1)
        return self.max_avg
