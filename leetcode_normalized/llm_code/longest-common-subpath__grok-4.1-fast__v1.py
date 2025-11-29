class C1:

    def longestCommonSubpath(self, a1, a2):

        def substr_hashes(a1, a2):
            v1 = len(a1)
            if a2 > v1:
                return set()
            v2 = [0] * (v1 + 1)
            v3 = [1] * (v1 + 1)
            v4 = [0] * (v1 + 1)
            v5 = [1] * (v1 + 1)
            v6, v7 = (131, 137)
            v8, v9 = (1000000007, 1000000009)
            for v10 in range(1, v1 + 1):
                v2[v10] = (v2[v10 - 1] * v6 + a1[v10 - 1]) % v8
                v3[v10] = v3[v10 - 1] * v6 % v8
                v4[v10] = (v4[v10 - 1] * v7 + a1[v10 - 1]) % v9
                v5[v10] = v5[v10 - 1] * v7 % v9
            v11 = set()
            for v12 in range(a2, v1 + 1):
                v13 = (v2[v12] - v2[v12 - a2] * v3[a2] % v8 + v8) % v8
                v14 = (v4[v12] - v4[v12 - a2] * v5[a2] % v9 + v9) % v9
                v11.add((v13, v14))
            return v11

        def feasible(a1):
            if a1 == 0:
                return True
            v1 = substr_hashes(a2[0], a1)
            for v2 in a2[1:]:
                v1 &= substr_hashes(v2, a1)
                if not v1:
                    return False
            return bool(v1)
        v1 = min((len(p) for v2 in a2))
        v3, v4 = (0, v1)
        while v3 < v4:
            v5 = (v3 + v4 + 1) // 2
            if feasible(v5):
                v3 = v5
            else:
                v4 = v5 - 1
        return v3
