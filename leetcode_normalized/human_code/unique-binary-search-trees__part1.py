class C1(object):

    def numTrees(self, a1):
        """
        """
        if a1 == 0:
            return 1

        def combination(a1, a2):
            v1 = 1
            for v2 in range(1, a2 + 1):
                v1 = v1 * (a1 - v2 + 1) / v2
            return v1
        return combination(2 * a1, a1) - combination(2 * a1, a1 - 1)
