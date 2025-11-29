class C1(object):

    def countSubarrays(self, a1):
        """
        """
        v1 = v2 = 1
        for v3 in range(1, len(a1)):
            if a1[v3 - 1] >= a1[v3]:
                v2 = 0
            v2 += 1
            v1 += v2
        return v1
