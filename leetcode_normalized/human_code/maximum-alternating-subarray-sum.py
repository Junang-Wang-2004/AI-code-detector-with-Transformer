class C1(object):

    def maximumAlternatingSubarraySum(self, a1):
        """
        """

        def kadane(a1, a2):
            v1 = float('-inf')
            v2 = v3 = 0
            for v4 in range(a2, len(a1)):
                v2 = v2 + a1[v4] if not v3 else max(v2 - a1[v4], 0)
                v1 = max(v1, v2)
                v3 ^= 1
            return v1
        return max(kadane(a1, 0), kadane(a1, 1))
