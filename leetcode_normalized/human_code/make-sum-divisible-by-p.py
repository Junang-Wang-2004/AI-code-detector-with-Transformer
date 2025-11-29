class C1(object):

    def minSubarray(self, a1, a2):
        """
        """
        v1 = sum(a1) % a2
        if not v1:
            return 0
        v2 = len(a1)
        v3, v4 = (0, {0: -1})
        for v5, v6 in enumerate(a1):
            v3 = (v3 + v6) % a2
            v4[v3] = v5
            if (v3 - v1) % a2 in v4:
                v2 = min(v2, v5 - v4[(v3 - v1) % a2])
        return v2 if v2 < len(a1) else -1
