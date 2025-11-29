class C1(object):

    def minimizeSet(self, a1, a2, a3, a4):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2

        def count(a1, a2, a3):
            v1 = lcm(a2, a3)
            return a1 + a1 // (v1 - 1) - int(a1 % (v1 - 1) == 0)
        return max(count(a3, a1, 1), count(a4, a2, 1), count(a3 + a4, a1, a2))
