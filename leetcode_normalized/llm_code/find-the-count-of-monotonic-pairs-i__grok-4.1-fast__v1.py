class C1(object):

    def countOfPairs(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = max(a1)
        v3 = [0] * (v2 + 1)
        for v4 in range(a1[0] + 1):
            v3[v4] = 1
        for v5 in range(1, len(a1)):
            v6 = max(0, a1[v5] - a1[v5 - 1])
            v7 = [0] * (v2 + 1)
            v8 = 0
            for v9 in range(v2 + 1):
                if v9 >= v6:
                    v8 = (v8 + v3[v9 - v6]) % v1
                if v9 <= a1[v5]:
                    v7[v9] = v8
            v3 = v7
        v10 = 0
        for v11 in v3:
            v10 = (v10 + v11) % v1
        return v10
