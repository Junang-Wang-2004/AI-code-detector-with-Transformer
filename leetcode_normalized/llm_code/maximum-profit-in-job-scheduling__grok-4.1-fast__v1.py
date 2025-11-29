import bisect

class C1:

    def jobScheduling(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [(a1[k], a2[k], a3[k]) for v3 in range(v1)]
        v2.sort(key=lambda t: t[1])
        v4 = []
        v5 = []
        v6 = 0
        for v7, v8, v9 in v2:
            v10 = bisect.bisect_right(v4, v7) - 1
            v11 = v5[v10] if v10 >= 0 else 0
            v12 = v11 + v9
            v13 = max(v6, v12)
            v4.append(v8)
            v5.append(v13)
            v6 = v13
        return v6
