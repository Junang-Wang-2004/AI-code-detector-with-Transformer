class C1(object):

    def maxIncreasingSubarrays(self, a1):
        """
        """
        v1 = 0
        v2, v3 = (1, 0)
        for v4 in range(len(a1) - 1):
            if a1[v4] < a1[v4 + 1]:
                v2 += 1
            else:
                v3 = v2
                v2 = 1
            v1 = max(v1, v2 // 2, min(v3, v2))
        return v1
