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

        def check(a1):
            return a1 - a1 // a1 >= a3 and a1 - a1 // a2 >= a4 and (a1 - a1 // l >= a3 + a4)
        v1 = lcm(a1, a2)
        v2, v3 = (2, 2 ** 31 - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v2
