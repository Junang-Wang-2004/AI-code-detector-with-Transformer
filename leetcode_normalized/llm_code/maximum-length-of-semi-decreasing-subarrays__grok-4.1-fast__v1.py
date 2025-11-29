class C1:

    def maxSubarrayLength(self, a1):
        v1 = len(a1)
        v2 = sorted(range(v1), key=lambda k: -a1[k])
        v3 = 0
        v4 = v1 - 1
        for v5 in range(v1):
            while v4 >= 0 and a1[v2[v4]] < a1[v5]:
                v6 = v2[v4]
                if v6 > v5:
                    v3 = max(v3, v6 - v5 + 1)
                v4 -= 1
        return v3
