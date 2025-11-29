class C1(object):

    def maxActiveSectionsAfterTrade(self, a1):
        """
        """
        v1 = v2 = v3 = v4 = 0
        for v5 in a1:
            if v5 == '0':
                v1 += 1
            else:
                if v1:
                    v2 = v1
                    v1 = 0
                v4 += 1
            v3 = max(v3, v2 + v1)
        return v4 if v3 in (v2, v1) else v3 + v4
