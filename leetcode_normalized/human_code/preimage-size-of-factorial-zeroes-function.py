class C1(object):

    def preimageSizeFZF(self, a1):
        """
        """

        def count_of_factorial_primes(a1, a2):
            v1 = 0
            while a1 > 0:
                v1 += a1 // a2
                a1 //= a2
            return v1
        v1 = 5
        v2, v3 = (0, v1 * a1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if count_of_factorial_primes(v4, v1) >= a1:
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v1 if count_of_factorial_primes(v2, v1) == a1 else 0
