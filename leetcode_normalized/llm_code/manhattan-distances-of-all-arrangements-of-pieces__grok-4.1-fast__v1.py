v1 = 10 ** 9 + 7

class C1:

    def distanceSum(self, a1, a2, a3):
        v1 = a1 * a2
        if a3 < 2:
            return 0

        def comb(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            v1 = 1
            for v2 in range(2, a1 + 1):
                v1 = v1 * v2 % v1
            v3 = 1
            for v2 in range(2, a2 + 1):
                v3 = v3 * v2 % v1
            v4 = 1
            for v2 in range(2, a1 - a2 + 1):
                v4 = v4 * v2 % v1
            v5 = pow(v3, v1 - 2, v1)
            v6 = pow(v4, v1 - 2, v1)
            return v1 * v5 % v1 * v6 % v1
        v2 = comb(v1 - 2, a3 - 2)

        def line_pairs(a1):
            return a1 * (a1 - 1) * (a1 + 1) // 6
        v3 = line_pairs(a1) * a2 * a2
        v4 = line_pairs(a2) * a1 * a1
        v5 = v3 + v4
        return v5 * v2 % v1
