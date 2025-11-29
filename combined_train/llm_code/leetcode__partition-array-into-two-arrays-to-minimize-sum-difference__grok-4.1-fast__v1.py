import bisect

class C1:

    def minimumDifference(self, a1):
        v1 = len(a1)
        v2 = v1 // 2
        v3 = a1[:v2]
        v4 = a1[v2:]

        def get_sums(a1):
            v1 = len(a1)
            v2 = [[] for v3 in range(v1 + 1)]

            def search(a1, a2, a3):
                if a1 == v1:
                    v2[a3].append(a2)
                    return
                search(a1 + 1, a2, a3)
                search(a1 + 1, a2 + a1[a1], a3 + 1)
            search(0, 0, 0)
            for v4 in range(v1 + 1):
                v2[v4].sort()
            return v2
        v5 = get_sums(v3)
        v6 = get_sums(v4)
        v7 = sum(a1)
        v8 = float('inf')
        for v9 in range(v2 + 1):
            v10 = v2 - v9
            v11 = v5[v9]
            v12 = v6[v10]
            for v13 in v11:
                v14 = v7 / 2 - v13
                v15 = bisect.bisect_left(v12, v14)
                for v16 in (v15 - 1, v15):
                    if 0 <= v16 < len(v12):
                        v17 = v12[v16]
                        v18 = abs(2 * (v13 + v17) - v7)
                        if v18 < v8:
                            v8 = v18
        return v8
