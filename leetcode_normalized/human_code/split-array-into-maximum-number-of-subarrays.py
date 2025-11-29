class C1(object):

    def maxSubarrays(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            v2 = v2 & v3 if v2 else v3
            if not v2:
                v1 += 1
        return max(v1, 1)
