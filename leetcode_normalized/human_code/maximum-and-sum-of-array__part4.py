class C1(object):

    def maximumANDSum(self, a1, a2):
        """
        """

        def memoiztion(a1, a2):
            if lookup[a2] != -1:
                return lookup[a2]
            v1 = a1[a1] if a1 < len(a1) else 0
            v2 = 1
            for v3 in range(1, a2 + 1):
                if a2 // v2 % 3:
                    lookup[a2] = max(lookup[a2], (v1 & v3) + memoiztion(a1 - 1, a2 - v2))
                v2 *= 3
            return lookup[a2]
        v1 = [-1] * 3 ** a2
        v1[0] = 0
        return memoiztion(2 * a2 - 1, 3 ** a2 - 1)
