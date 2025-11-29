class C1(object):

    def countSubarrays(self, a1, a2, a3):
        """
        """
        v1 = v2 = 0
        v3 = [-1] * 2
        for v4, v5 in enumerate(a1):
            if not a2 <= v5 <= a3:
                v2 = v4 + 1
                continue
            if v5 == a2:
                v3[0] = v4
            if v5 == a3:
                v3[1] = v4
            v1 += max(min(v3) - v2 + 1, 0)
        return v1
