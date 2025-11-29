class C1(object):

    def commonFactors(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = gcd(a1, a2)
        v2 = 0
        v3 = 1
        while v3 * v3 <= v1:
            if v1 % v3 == 0:
                v2 += 1 if v1 // v3 == v3 else 2
            v3 += 1
        return v2
