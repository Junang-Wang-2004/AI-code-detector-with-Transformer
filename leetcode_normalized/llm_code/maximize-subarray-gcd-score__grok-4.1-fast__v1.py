from bisect import bisect_left, bisect_right

class C1:

    def maxGCDScore(self, a1, a2):
        if not a1:
            return 0
        v1 = len(a1)
        v2 = [0] * v1
        v3 = [0] * v1
        for v4 in range(v1):
            v5 = a1[v4]
            v6 = 0
            while v5 % 2 == 0 and v5 > 0:
                v5 //= 2
                v6 += 1
            v2[v4] = v6
            v3[v4] = v5
        v7 = max(v2, default=0)
        v8 = [[] for v9 in range(v7 + 1)]
        for v4, v10 in enumerate(v2):
            v8[v10].append(v4)

        def compute_gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v11 = {}
        v12 = 0
        for v13 in range(v1):
            v14 = v3[v13]
            v15 = v2[v13]
            v16 = {}
            v17 = (v14, v15)
            v16[v17] = [v13, v13]
            for v18, v19 in v11.items():
                v20, v21 = v18
                v22 = compute_gcd(v20, v14)
                v23 = min(v21, v15)
                v24 = (v22, v23)
                if v24 not in v16:
                    v16[v24] = [float('inf'), float('inf')]
                v16[v24][0] = min(v16[v24][0], v19[0])
                v25 = v8[v23]
                v26 = bisect_left(v25, v19[0])
                v27 = bisect_right(v25, v13) - 1
                v28 = max(0, v27 - v26 + 1)
                v29 = v19[0] if v28 <= a2 else v25[v27 - a2] + 1
                v16[v24][1] = min(v16[v24][1], v29)
            v11 = v16
            for v30, v31 in v11.items():
                v32, v33 = v30
                v34 = v13 - v31[0] + 1
                v35 = v32 * v34 * (1 << v33)
                v12 = max(v12, v35)
                if v31[1] <= v13:
                    v36 = v13 - v31[1] + 1
                    v37 = v32 * v36 * (1 << v33 + 1)
                    v12 = max(v12, v37)
        return v12
