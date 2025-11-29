class C1:

    def numberOfPermutations(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = {}
        v3 = 0
        for v4, v5 in a2:
            v2[v4] = v5
            if v5 > v3:
                v3 = v5
        v6 = [0] * (v3 + 1)
        v6[0] = 1
        for v7 in range(a1):
            v8 = [0] * (v3 + 1)
            v9 = v7 + 1
            v10 = 0
            for v11 in range(v3 + 1):
                v10 = (v10 + v6[v11]) % v1
                v12 = v11 - v9
                if v12 >= 0:
                    v10 = (v10 - v6[v12] + v1) % v1
                if v7 not in v2 or v11 == v2[v7]:
                    v8[v11] = v10
            v6 = v8
        return v6[v3]
