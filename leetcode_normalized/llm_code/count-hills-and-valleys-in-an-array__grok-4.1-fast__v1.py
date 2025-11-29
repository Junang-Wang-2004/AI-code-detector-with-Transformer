class C1:

    def countHillValley(self, a1):
        v1 = 0
        v2 = 0
        for v3 in range(len(a1) - 1):
            v4 = a1[v3 + 1] - a1[v3]
            if v4 != 0:
                v5 = 1 if v4 > 0 else -1
                if v2 != 0 and v5 != v2:
                    v1 += 1
                v2 = v5
        return v1
