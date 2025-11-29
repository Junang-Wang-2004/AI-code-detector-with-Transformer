class C1:

    def maxNumberOfApples(self, a1):
        v1 = 5000
        v2 = sorted(a1)
        v3 = 0
        v4 = 0
        while v4 < len(v2) and v3 + v2[v4] <= v1:
            v3 += v2[v4]
            v4 += 1
        return v4
