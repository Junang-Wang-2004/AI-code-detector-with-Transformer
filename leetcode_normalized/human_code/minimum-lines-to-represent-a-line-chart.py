class C1(object):

    def minimumLines(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        a1.sort()
        v1 = 0
        v2 = None
        for v3 in range(1, len(a1)):
            v4, v5 = (a1[v3][1] - a1[v3 - 1][1], a1[v3][0] - a1[v3 - 1][0])
            v6 = gcd(v4, v5)
            if not v2 or v2 != (v4 // v6, v5 // v6):
                v2 = (v4 // v6, v5 // v6)
                v1 += 1
        return v1
