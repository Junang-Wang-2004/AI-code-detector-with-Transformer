import bisect

class C1:

    def lengthOfLIS(self, a1, a2):
        v1 = sorted(set((x - 1 for v2 in a1)))
        if not v1:
            return 0
        v3 = {v: i for v4, v5 in enumerate(v1)}
        v6 = len(v1)
        v7 = [0] * (4 * v6)

        def upd(a1, a2, a3=1, a4=0, a5=v6 - 1):
            if a4 == a5:
                v7[a3] = max(v7[a3], a2)
                return
            v1 = (a4 + a5) // 2
            if a1 <= v1:
                upd(a1, a2, a3 * 2, a4, v1)
            else:
                upd(a1, a2, a3 * 2 + 1, v1 + 1, a5)
            v7[a3] = max(v7[a3 * 2], v7[a3 * 2 + 1])

        def qry(a1, a2, a3=1, a4=0, a5=v6 - 1):
            if a1 > a5 or a2 < a4:
                return 0
            if a1 <= a4 and a5 <= a2:
                return v7[a3]
            v1 = (a4 + a5) // 2
            return max(qry(a1, a2, a3 * 2, a4, v1), qry(a1, a2, a3 * 2 + 1, v1 + 1, a5))
        v8 = 0
        for v9 in a1:
            v10 = v9 - 1
            if v10 not in v3:
                continue
            v11 = v3[v10]
            v12 = bisect.bisect_left(v1, v10 - a2)
            v13 = qry(v12, v11 - 1) if v12 < v11 else 0
            upd(v11, v13 + 1)
            v8 = max(v8, v13 + 1)
        return v8
