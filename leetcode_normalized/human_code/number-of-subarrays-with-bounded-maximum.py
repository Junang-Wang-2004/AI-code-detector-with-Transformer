class C1(object):

    def numSubarrayBoundedMax(self, a1, a2, a3):
        """
        """

        def count(a1, a2):
            v1, v2 = (0, 0)
            for v3 in a1:
                v2 = v2 + 1 if v3 <= a2 else 0
                v1 += v2
            return v1
        return count(a1, a3) - count(a1, a2 - 1)
