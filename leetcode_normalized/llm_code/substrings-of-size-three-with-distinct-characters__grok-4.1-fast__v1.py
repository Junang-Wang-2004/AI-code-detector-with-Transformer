class C1(object):

    def countGoodSubstrings(self, a1):
        v1 = 0
        v2 = len(a1)
        for v3 in range(v2 - 2):
            v4, v5, v6 = (a1[v3], a1[v3 + 1], a1[v3 + 2])
            if v4 != v5 and v4 != v6 and (v5 != v6):
                v1 += 1
        return v1
