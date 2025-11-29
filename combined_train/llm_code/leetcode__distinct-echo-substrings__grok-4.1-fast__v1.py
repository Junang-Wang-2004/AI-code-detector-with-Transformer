class C1:

    def distinctEchoSubstrings(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = 1000000007
        v3 = 31
        v4 = 1000000009
        v5 = 37
        v6 = [0] * (v1 + 1)
        v7 = [0] * (v1 + 1)
        v8 = [1] * (v1 + 1)
        v9 = [1] * (v1 + 1)
        for v10 in range(v1):
            v11 = ord(a1[v10]) - ord('a') + 1
            v6[v10 + 1] = (v6[v10] * v3 + v11) % v2
            v7[v10 + 1] = (v7[v10] * v5 + v11) % v4
            v8[v10 + 1] = v8[v10] * v3 % v2
            v9[v10 + 1] = v9[v10] * v5 % v4

        def substr_hash1(a1, a2):
            v1 = (v6[a2] - v6[a1] * v8[a2 - a1] % v2 + v2) % v2
            return v1

        def substr_hash2(a1, a2):
            v1 = (v7[a2] - v7[a1] * v9[a2 - a1] % v4 + v4) % v4
            return v1
        v12 = set()
        for v13 in range(1, v1 // 2 + 1):
            for v14 in range(v1 - 2 * v13 + 1):
                v15 = substr_hash1(v14, v14 + v13)
                v16 = substr_hash1(v14 + v13, v14 + 2 * v13)
                v17 = substr_hash2(v14, v14 + v13)
                v18 = substr_hash2(v14 + v13, v14 + 2 * v13)
                if v15 == v16 and v17 == v18:
                    v12.add((v15, v17))
        return len(v12)
