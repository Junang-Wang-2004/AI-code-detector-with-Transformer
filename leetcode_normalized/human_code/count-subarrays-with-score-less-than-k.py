class C1(object):

    def countSubarrays(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            v2 += a1[v4]
            while v2 * (v4 - v3 + 1) >= a2:
                v2 -= a1[v3]
                v3 += 1
            v1 += v4 - v3 + 1
        return v1
