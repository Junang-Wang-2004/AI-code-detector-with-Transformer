class C1(object):

    def sumOfGoodSubsequences(self, a1):
        v1 = 10 ** 9 + 7
        v2 = {}
        v3 = {}
        for v4 in a1:
            v5 = v2.get(v4 - 1, 0)
            v6 = v2.get(v4 + 1, 0)
            v7 = (v5 + v6 + 1) % v1
            v2[v4] = (v2.get(v4, 0) + v7) % v1
            v8 = v3.get(v4 - 1, 0)
            v9 = v3.get(v4 + 1, 0)
            v10 = (v8 + v9 + v4 * v7 % v1) % v1
            v3[v4] = (v3.get(v4, 0) + v10) % v1
        v11 = 0
        for v12 in v3.values():
            v11 = (v11 + v12) % v1
        return v11
