class C1(object):

    def largestBSTSubtree(self, a1):
        """
        """
        if a1 is None:
            return 0
        v1 = [1]

        def largestBSTSubtreeHelper(a1):
            if a1.left is None and a1.right is None:
                return (1, a1.val, a1.val)
            v1, v2, v3 = (0, a1.val, a1.val)
            if a1.left is not None:
                v1, v2, v3 = largestBSTSubtreeHelper(a1.left)
            v4, v5, v6 = (0, a1.val, a1.val)
            if a1.right is not None:
                v4, v5, v6 = largestBSTSubtreeHelper(a1.right)
            v7 = 0
            if (a1.left is None or v1 > 0) and (a1.right is None or v4 > 0) and (v3 <= a1.val <= v5):
                v7 = 1 + v1 + v4
                v1[0] = max(v1[0], v7)
            return (v7, v2, v6)
        largestBSTSubtreeHelper(a1)
        return v1[0]
