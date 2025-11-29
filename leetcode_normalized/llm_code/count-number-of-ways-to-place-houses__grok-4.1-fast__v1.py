class C1:

    def countHousePlacements(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 1
        v3 = 2
        for v4 in range(2, a1 + 1):
            v5 = (v2 + v3) % v1
            v2 = v3
            v3 = v5
        return pow(v3, 2, v1)
