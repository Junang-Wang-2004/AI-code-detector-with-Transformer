class C1(object):

    def subarrayGCD(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = 0
        for v2 in range(len(a1)):
            v3 = 0
            for v4 in range(v2, len(a1)):
                if a1[v4] % a2:
                    break
                v3 = gcd(v3, a1[v4])
                v1 += int(v3 == a2)
        return v1
