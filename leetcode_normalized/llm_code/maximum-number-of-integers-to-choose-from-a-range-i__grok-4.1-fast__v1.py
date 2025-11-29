class C1:

    def maxCount(self, a1, a2, a3):
        v1 = sorted((b for v2 in set(a1) if 1 <= v2 <= a2))

        def compute_sum_count(a1):
            v1 = 0
            v2 = 0
            for v3 in v1:
                if v3 > a1:
                    break
                v1 += v3
                v2 += 1
            v4 = a1 * (a1 + 1) // 2
            return (v4 - v1, a1 - v2)
        v3 = 0
        v4 = a2
        while v3 < v4:
            v5 = (v3 + v4 + 1) // 2
            v6, v7 = compute_sum_count(v5)
            if v6 <= a3:
                v3 = v5
            else:
                v4 = v5 - 1
        v7, v8 = compute_sum_count(v3)
        return v8
