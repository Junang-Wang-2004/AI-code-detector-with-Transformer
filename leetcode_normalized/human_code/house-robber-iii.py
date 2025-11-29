class C1(object):

    def rob(self, a1):
        """
        """

        def robHelper(a1):
            if not a1:
                return (0, 0)
            v1, v2 = (robHelper(a1.left), robHelper(a1.right))
            return (a1.val + v1[1] + v2[1], max(v1) + max(v2))
        return max(robHelper(a1))
