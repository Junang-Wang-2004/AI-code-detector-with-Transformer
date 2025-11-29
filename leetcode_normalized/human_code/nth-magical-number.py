class C1(object):

    def nthMagicalNumber(self, a1, a2, a3):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def check(a1, a2, a3, a4, a5):
            return a5 // a1 + a5 // a2 - a5 // a4 >= a3
        v1 = a2 * a3 // gcd(a2, a3)
        v2, v3 = (min(a2, a3), max(a2, a3) * a1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(a2, a3, a1, v1, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v2 % (10 ** 9 + 7)
