class C1:

    def hasSameDigits(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return True
        v2 = v1 - 2

        def small_c(a1, a2, a3):
            if a2 > a1:
                return 0
            if a2 > a1 - a2:
                a2 = a1 - a2
            v2 = 1
            for v3 in range(1, a2 + 1):
                v2 = v2 * (a1 - v3 + 1) // v3
            return v2 % a3

        def lucas_theorem(a1, a2, a3):
            if a2 < 0 or a2 > a1:
                return 0
            v1 = 1
            v2 = a1
            v3 = a2
            while v2 > 0 or v3 > 0:
                v4 = v2 % a3
                v5 = v3 % a3
                if v5 > v4:
                    return 0
                v1 = v1 * small_c(v4, v5, a3) % a3
                v2 //= a3
                v3 //= a3
            return v1

        def coeff_mod10(a1, a2):
            v1 = lucas_theorem(a1, a2, 2)
            v2 = lucas_theorem(a1, a2, 5)
            for v3 in range(10):
                if v3 % 2 == v1 and v3 % 5 == v2:
                    return v3
            return 0
        v3 = 0
        for v4 in range(v2 + 1):
            v5 = coeff_mod10(v2, v4)
            v6 = ord(a1[v4]) - ord(a1[v4 + 1])
            v3 = (v3 + v5 * v6) % 10
        return v3 == 0
