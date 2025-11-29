class C1:

    def minValidStrings(self, a1, a2):
        v1 = len(a2)
        v2 = ord('a')
        v3 = 1000000007
        v4 = 131
        v5 = 1000000009
        v6 = 137
        v7 = [1] * (v1 + 1)
        v8 = [1] * (v1 + 1)
        for v9 in range(1, v1 + 1):
            v7[v9] = v7[v9 - 1] * v4 % v3
            v8[v9] = v8[v9 - 1] * v6 % v5
        v10 = set()
        for v11 in a1:
            v12 = 0
            v13 = 0
            for v14 in v11:
                v15 = ord(v14) - v2 + 1
                v12 = (v12 * v4 + v15) % v3
                v13 = (v13 * v6 + v15) % v5
                v10.add((v12, v13))
        v16 = [0] * (v1 + 1)
        v17 = 0
        v18 = 0
        v19 = 0
        for v20 in range(v1):
            v21 = ord(a2[v20]) - v2 + 1
            v17 = (v17 * v4 + v21) % v3
            v18 = (v18 * v6 + v21) % v5
            while v19 <= v20 and (v17, v18) not in v10:
                v22 = ord(a2[v19]) - v2 + 1
                v23 = v7[v20 - v19]
                v17 = (v17 - v22 * v23 % v3 + v3) % v3
                v24 = v8[v20 - v19]
                v18 = (v18 - v22 * v24 % v5 + v5) % v5
                v19 += 1
            if v19 > v20:
                return -1
            v16[v20 + 1] = v16[v19] + 1
        return v16[v1]
