class C1(object):

    def countPairs(self, a1, a2):
        a1 = sorted(a1)
        v2 = len(a1)
        v3 = 0
        v4 = v2 - 1
        for v5 in range(v2 - 1):
            while v5 < v4 and a1[v5] + a1[v4] >= a2:
                v4 -= 1
            v3 += max(0, v4 - v5)
        return v3
