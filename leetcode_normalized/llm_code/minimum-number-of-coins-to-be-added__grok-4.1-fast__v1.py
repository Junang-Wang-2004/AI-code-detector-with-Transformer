class C1:

    def minimumAddedCoins(self, a1, a2):
        a1.sort()
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v2 < a2:
            if v3 < v4 and a1[v3] <= v2 + 1:
                v2 += a1[v3]
                v3 += 1
            else:
                v1 += 1
                v2 = 2 * v2 + 1
        return v1
