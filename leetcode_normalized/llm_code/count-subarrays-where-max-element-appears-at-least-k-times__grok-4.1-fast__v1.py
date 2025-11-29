class C1:

    def countSubarrays(self, a1, a2):
        v1 = len(a1)
        v2 = max(a1)
        v3 = v1 * (v1 + 1) // 2
        v4 = 0
        v5 = 0
        v6 = 0
        for v7 in range(v1):
            if a1[v7] == v2:
                v6 += 1
            while v6 > a2 - 1 and v5 <= v7:
                if a1[v5] == v2:
                    v6 -= 1
                v5 += 1
            v4 += v7 - v5 + 1
        return v3 - v4
