class C1(object):

    def maxAncestorDiff(self, a1):
        """
        """

        def maxAncestorDiffHelper(a1, a2, a3):
            if not a1:
                return 0
            v1 = max(a2 - a1.val, a1.val - a3)
            a2 = max(a2, a1.val)
            a3 = min(a3, a1.val)
            v1 = max(v1, maxAncestorDiffHelper(a1.left, a2, a3))
            v1 = max(v1, maxAncestorDiffHelper(a1.right, a2, a3))
            return v1
        return maxAncestorDiffHelper(a1, 0, float('inf'))
