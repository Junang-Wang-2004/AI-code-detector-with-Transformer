import bisect

class C1:

    def minimumSumSubarray(self, a1, a2, a3):
        v1 = float('inf')
        v2 = float('-inf')
        v3 = len(a1)
        v4 = [0] * (v3 + 1)
        for v5 in range(v3):
            v4[v5 + 1] = v4[v5] + a1[v5]
        v6 = sorted(set(v4))
        v7 = len(v6)
        if v7 == 0:
            return -1
        v8 = {v6[j]: j for v9 in range(v7)}
        v10 = [v2] * (4 * v7)
        v11 = [0] * v7

        def update_tree(a1, a2, a3, a4, a5):
            if a2 == a3:
                v10[a1] = a5
                return
            v1 = (a2 + a3) // 2
            if a4 <= v1:
                update_tree(2 * a1, a2, v1, a4, a5)
            else:
                update_tree(2 * a1 + 1, v1 + 1, a3, a4, a5)
            v10[a1] = max(v10[2 * a1], v10[2 * a1 + 1])

        def query_tree(a1, a2, a3, a4, a5):
            if a5 < a2 or a3 < a4:
                return v2
            if a4 <= a2 and a3 <= a5:
                return v10[a1]
            v1 = (a2 + a3) // 2
            v2 = query_tree(2 * a1, a2, v1, a4, a5)
            v3 = query_tree(2 * a1 + 1, v1 + 1, a3, a4, a5)
            return max(v2, v3)
        v12 = v1
        for v5 in range(v3):
            v13 = v5 - a2 + 1
            if v13 >= 0:
                v14 = v8[v4[v13]]
                v11[v14] += 1
                if v11[v14] == 1:
                    update_tree(1, 0, v7 - 1, v14, v6[v14])
            v15 = v5 - a3
            if v15 >= 0:
                v14 = v8[v4[v15]]
                v11[v14] -= 1
                if v11[v14] == 0:
                    update_tree(1, 0, v7 - 1, v14, v2)
            v16 = v4[v5 + 1]
            v17 = bisect.bisect_left(v6, v16) - 1
            if v17 >= 0:
                v18 = query_tree(1, 0, v7 - 1, 0, v17)
                if v18 != v2:
                    v12 = min(v12, v16 - v18)
        return v12 if v12 < v1 else -1
