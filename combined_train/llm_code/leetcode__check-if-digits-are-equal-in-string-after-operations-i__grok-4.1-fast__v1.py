class C1:

    def hasSameDigits(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return True
        v2 = [int(c) for v3 in a1]
        v4 = [v2[j] - v2[j + 1] for v5 in range(v1 - 1)]
        v6 = v1 - 2

        def sum_mod_prime(a1):
            v1 = 0
            for v2 in range(v6 + 1):
                v3 = lucas(v6, v2, a1)
                v1 = (v1 + v3 * (v4[v2] % a1)) % a1
            return v1

        def lucas(a1, a2, a3):
            if a2 < 0 or a2 > a1:
                return 0
            v1 = 1
            while a1 or a2:
                v2 = a1 % a3
                v3 = a2 % a3
                if v3 > v2:
                    return 0
                v1 = v1 * small_binom(v2, v3) % a3
                a1 //= a3
                a2 //= a3
            return v1

        def small_binom(a1, a2):
            if a2 > a1 - a2:
                a2 = a1 - a2
            if a2 == 0:
                return 1
            v2 = 1
            for v3 in range(1, a2 + 1):
                v2 *= a1 - v3 + 1
                v2 //= v3
            return v2
        return sum_mod_prime(2) == 0 and sum_mod_prime(5) == 0
