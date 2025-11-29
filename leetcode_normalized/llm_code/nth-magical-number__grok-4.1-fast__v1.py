class C1:

    def nthMagicalNumber(self, a1, a2, a3):

        def get_gcd(a1, a2):
            return a1 if a2 == 0 else get_gcd(a2, a1 % a2)
        v1 = a2 * a3 // get_gcd(a2, a3)

        def count_divisible_by_a_or_b(a1):
            return a1 // a2 + a1 // a3 - a1 // v1
        v2, v3 = (1, 10 ** 18)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if count_divisible_by_a_or_b(v4) >= a1:
                v3 = v4
            else:
                v2 = v4 + 1
        return v2 % (10 ** 9 + 7)
