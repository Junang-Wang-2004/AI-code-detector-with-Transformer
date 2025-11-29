class C1(object):

    def countPairs(self, a1):
        v1 = 10 ** 9 + 7
        v2 = max(a1)
        v3 = []
        v4 = 1
        while v4 <= 2 * v2:
            v3.append(v4)
            v4 *= 2
        v5 = {}
        v6 = 0
        for v7 in a1:
            for v8 in v3:
                v9 = v8 - v7
                v6 = (v6 + v5.get(v9, 0)) % v1
            v5[v7] = v5.get(v7, 0) + 1
        return v6
