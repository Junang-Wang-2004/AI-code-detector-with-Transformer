class C1:

    def maxActiveSectionsAfterTrade(self, a1):
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = len(a1)
        while v4 < v5:
            if a1[v4] == '1':
                v1 += 1
                v4 += 1
                continue
            v6 = 0
            while v4 < v5 and a1[v4] == '0':
                v6 += 1
                v4 += 1
            if v3 > 0:
                v2 = max(v2, v3 + v6)
            v3 = v6
        return v1 + v2
