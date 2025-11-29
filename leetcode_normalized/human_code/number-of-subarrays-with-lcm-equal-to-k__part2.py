class C1(object):

    def subarrayLCM(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2
        v1 = 0
        for v2 in range(len(a1)):
            v3 = 1
            for v4 in range(v2, len(a1)):
                if a2 % a1[v4]:
                    break
                v3 = lcm(v3, a1[v4])
                v1 += int(v3 == a2)
        return v1
