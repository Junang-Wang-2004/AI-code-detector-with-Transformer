class C1:

    def countSubarrays(self, a1, a2, a3):
        v1 = 0
        v2 = 0
        v3 = -1
        v4 = -1
        for v5, v6 in enumerate(a1):
            if v6 < a2 or v6 > a3:
                v2 = v5 + 1
                v3 = -1
                v4 = -1
            if v6 == a2:
                v3 = v5
            if v6 == a3:
                v4 = v5
            if v3 >= 0 and v4 >= 0:
                v1 += min(v3, v4) - v2 + 1
        return v1
