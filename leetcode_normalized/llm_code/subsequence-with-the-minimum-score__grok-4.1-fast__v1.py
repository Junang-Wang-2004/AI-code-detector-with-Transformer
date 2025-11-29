class C1(object):

    def minimumScore(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = [0] * v1
        v4 = 0
        for v5 in range(v1 - 1, -1, -1):
            if v4 < v2 and a1[v5] == a2[v2 - 1 - v4]:
                v4 += 1
            v3[v5] = v4
        v6 = v2 - v4
        v7 = 0
        for v5 in range(v1):
            v8 = v7 + v3[v5]
            v6 = min(v6, v2 - min(v2, v8))
            if v7 < v2 and a1[v5] == a2[v7]:
                v7 += 1
        v6 = min(v6, v2 - v7)
        return v6
