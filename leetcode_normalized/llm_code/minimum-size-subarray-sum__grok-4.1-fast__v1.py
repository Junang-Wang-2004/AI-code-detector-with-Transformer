class C1:

    def minSubArrayLen(self, a1, a2):
        v1 = len(a2)
        v2 = v1 + 1
        v3 = 0
        v4 = 0
        v5 = 0
        while v5 < v1:
            v3 += a2[v5]
            while v3 >= a1:
                v2 = min(v2, v5 - v4 + 1)
                v3 -= a2[v4]
                v4 += 1
            v5 += 1
        return v2 if v2 <= v1 else 0
