class C1:

    def countSubarrays(self, a1):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = v2
            while v4 + 1 < v3 and a1[v4] < a1[v4 + 1]:
                v4 += 1
            v5 = v4 - v2 + 1
            v1 += v5 * (v5 + 1) // 2
            v2 = v4 + 1
        return v1
