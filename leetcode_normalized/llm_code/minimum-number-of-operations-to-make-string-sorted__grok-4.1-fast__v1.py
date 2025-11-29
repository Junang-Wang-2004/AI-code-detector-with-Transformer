class C1:

    def makeStringSorted(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [1] * (v2 + 1)
        for v4 in range(1, v2 + 1):
            v3[v4] = v3[v4 - 1] * v4 % v1
        v5 = [0] * (v2 + 1)
        v5[v2] = pow(v3[v2], v1 - 2, v1)
        for v4 in range(v2 - 1, -1, -1):
            v5[v4] = v5[v4 + 1] * (v4 + 1) % v1
        v6 = [0] * 26
        for v7 in a1:
            v6[ord(v7) - ord('a')] += 1
        v8 = 1
        for v9 in range(26):
            v8 = v8 * v5[v6[v9]] % v1
        v10 = 0
        v11 = v2
        for v4 in range(v2):
            v12 = ord(a1[v4]) - ord('a')
            v13 = 0
            for v9 in range(v12):
                v13 += v6[v9]
            if v13:
                v14 = v3[v11] * v8 % v1
                v15 = v13 * v14 % v1 * pow(v11, v1 - 2, v1) % v1
                v10 = (v10 + v15) % v1
            v16 = v6[v12]
            v6[v12] -= 1
            v8 = v8 * v3[v16] % v1 * v5[v16 - 1] % v1
            v11 -= 1
        return v10
