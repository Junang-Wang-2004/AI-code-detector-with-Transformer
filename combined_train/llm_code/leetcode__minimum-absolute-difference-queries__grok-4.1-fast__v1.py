class C1:

    def minDifference(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return []
        v2 = max(a1)
        v3 = int(v1 ** 0.5) + 1
        v4 = [(l // v3, r, i, l, r) for v5, (v6, v7) in enumerate(a2)]
        v4.sort()
        v8 = [0] * len(a2)
        v9 = [0] * (v2 + 1)
        v10 = 0
        v11 = -1

        def insert(a1):
            v9[a1[a1]] += 1

        def delete(a1):
            v9[a1[a1]] -= 1
        for v12, v13, v14, v15, v16 in v4:
            while v11 < v16:
                v11 += 1
                insert(v11)
            while v10 > v15:
                v10 -= 1
                insert(v10)
            while v11 > v16:
                delete(v11)
                v11 -= 1
            while v10 < v15:
                delete(v10)
                v10 += 1
            v17 = float('inf')
            v18 = -1
            for v19 in range(v2 + 1):
                if v9[v19] > 0:
                    if v18 != -1:
                        v17 = min(v17, v19 - v18)
                    v18 = v19
            v8[v14] = v17 if v17 != float('inf') else -1
        return v8
