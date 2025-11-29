import bisect

class C1:

    def numberOfPairs(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [a1[i] - a2[i] for v3 in range(v1)]
        v4 = sorted(set(v2))
        v5 = len(v4)
        v6 = {v4[j]: j for v7 in range(v5)}
        v8 = [0] * (v5 + 2)

        def modify(a1, a2):
            a1 += 1
            while a1 <= v5:
                v8[a1] += a2
                a1 += a1 & -a1

        def inquire(a1):
            a1 += 1
            v2 = 0
            while a1 > 0:
                v2 += v8[a1]
                a1 -= a1 & -a1
            return v2
        v9 = 0
        for v10 in v2:
            v11 = bisect.bisect_right(v4, v10 + a3) - 1
            if v11 >= 0:
                v9 += inquire(v11)
            modify(v6[v10], 1)
        return v9
