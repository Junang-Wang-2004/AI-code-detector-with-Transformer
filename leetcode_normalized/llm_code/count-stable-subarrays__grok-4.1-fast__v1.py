class C1:

    def countStableSubarrays(self, a1, a2):
        v1 = len(a1)
        v2 = []
        v3 = []
        v4 = 0
        while v4 < v1:
            v5 = v4
            while v5 + 1 < v1 and a1[v5] <= a1[v5 + 1]:
                v5 += 1
            v2.append(v4)
            v3.append(v5)
            v4 = v5 + 1
        v6 = len(v2)
        v7 = [0] * v6
        v8 = [0] * (v6 + 1)
        for v9 in range(v6):
            v10 = v3[v9] - v2[v9] + 1
            v7[v9] = v10 * (v10 + 1) // 2
            v8[v9 + 1] = v8[v9] + v7[v9]
        v11 = [-1] * v1
        for v9 in range(v6):
            for v12 in range(v2[v9], v3[v9] + 1):
                v11[v12] = v9
        v13 = []
        for v14, v15 in a2:
            v16 = v11[v14]
            v17 = v11[v15]
            if v16 == v17:
                v18 = v15 - v14 + 1
                v19 = v18 * (v18 + 1) // 2
            else:
                v20 = v3[v16]
                v21 = v20 - v14 + 1
                v22 = v21 * (v21 + 1) // 2
                v23 = v2[v17]
                v24 = v15 - v23 + 1
                v25 = v24 * (v24 + 1) // 2
                v26 = v8[v17] - v8[v16 + 1]
                v19 = v22 + v26 + v25
            v13.append(v19)
        return v13
