class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maximumAverageSubtree(self, a1):
        """
        """

        def maximumAverageSubtreeHelper(a1, a2):
            if not a1:
                return [0.0, 0]
            v1, v2 = maximumAverageSubtreeHelper(a1.left, a2)
            v3, v4 = maximumAverageSubtreeHelper(a1.right, a2)
            v5 = v1 + v3 + a1.val
            v6 = v2 + v4 + 1
            a2[0] = max(a2[0], v5 / v6)
            return [v5, v6]
        v1 = [0]
        maximumAverageSubtreeHelper(a1, v1)
        return v1[0]
