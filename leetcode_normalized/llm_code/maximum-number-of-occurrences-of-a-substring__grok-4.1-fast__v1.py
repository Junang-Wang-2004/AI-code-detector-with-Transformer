class C1:

    def maxFreq(self, a1: str, a2: int, a3: int, a4: int) -> int:
        v1 = len(a1)
        v2 = a3
        if v1 < v2:
            return 0
        v3, v4 = (1000000007, 131)
        v5, v6 = (1000000009, 137)
        v7 = [1] * (v1 + 1)
        v8 = [1] * (v1 + 1)
        v9 = [0] * (v1 + 1)
        v10 = [0] * (v1 + 1)
        for v11 in range(v1):
            v12 = ord(a1[v11]) - ord('a') + 1
            v9[v11 + 1] = (v9[v11] * v4 + v12) % v3
            v7[v11 + 1] = v7[v11] * v4 % v3
            v10[v11 + 1] = (v10[v11] * v6 + v12) % v5
            v8[v11 + 1] = v8[v11] * v6 % v5
        v13 = {}
        v14 = {}
        v15 = 0
        v16 = 0
        for v17 in range(v1):
            v13[a1[v17]] = v13.get(a1[v17], 0) + 1
            while v17 - v15 + 1 > v2:
                v13[a1[v15]] -= 1
                if v13[a1[v15]] == 0:
                    del v13[a1[v15]]
                v15 += 1
            if v17 - v15 + 1 == v2 and len(v13) <= a2:
                v18 = v2
                v19 = (v9[v17 + 1] - v9[v15] * v7[v18] % v3 + v3) % v3
                v20 = (v10[v17 + 1] - v10[v15] * v8[v18] % v5 + v5) % v5
                v21 = (v19, v20)
                v22 = v14.get(v21, 0) + 1
                v14[v21] = v22
                if v22 > v16:
                    v16 = v22
        return v16
