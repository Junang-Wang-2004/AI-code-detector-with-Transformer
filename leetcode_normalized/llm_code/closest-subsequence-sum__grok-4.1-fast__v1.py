import bisect

class C1:

    def minAbsDifference(self, a1, a2):
        v1 = sum((x for v2 in a1 if v2 > 0))
        v3 = sum((v2 for v2 in a1 if v2 < 0))
        if a2 > v1:
            return a2 - v1
        if a2 < v3:
            return v3 - a2
        v4 = len(a1) // 2
        v5 = a1[:v4]
        v6 = a1[v4:]

        def all_sums(a1):
            v1 = [0]
            for v2 in a1:
                v3 = [t + v2 for v4 in v1]
                v1.extend(v3)
            return v1
        v7 = sorted(all_sums(v5))
        v8 = all_sums(v6)
        v9 = abs(a2)
        for v10 in v8:
            v11 = a2 - v10
            v12 = bisect.bisect_left(v7, v11)
            if v12 < len(v7):
                v9 = min(v9, abs(v7[v12] - v11))
            if v12 > 0:
                v9 = min(v9, abs(v7[v12 - 1] - v11))
            if v9 == 0:
                return 0
        return v9
