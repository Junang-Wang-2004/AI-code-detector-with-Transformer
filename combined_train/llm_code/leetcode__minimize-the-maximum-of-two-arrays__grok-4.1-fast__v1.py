class C1:

    def minimizeSet(self, a1, a2, a3, a4):

        def gcd(a1, a2):
            while a2 != 0:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            v1 = gcd(a1, a2)
            return a1 // v1 * a2

        def required_size(a1, a2):
            if a2 == 0:
                return 0
            v1 = a1 - 1
            v2 = a2 // v1
            v3 = a2 % v1
            if v3 == 0:
                return v2 * a1 - 1
            return v2 * a1 + v3
        v1 = lcm(a1, a2)
        v2 = required_size(a1, a3)
        v3 = required_size(a2, a4)
        v4 = required_size(v1, a3 + a4)
        return max(v2, v3, v4)
