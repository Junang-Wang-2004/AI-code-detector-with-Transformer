class C1(object):

    def hasSameDigits(self, a1):
        """
        """

        def check(a1):

            def decompose(a1, a2):
                v1 = 0
                while a1 > 1 and a1 % a2 == 0:
                    a1 //= a2
                    v1 += 1
                return (a1, v1)
            v1 = v2 = 0
            v3 = 1
            for v4 in range(len(a1) - 1):
                if v2 == 0:
                    v1 = (v1 + v3 * (ord(a1[v4]) - ord(a1[v4 + 1]))) % a1
                v5, v6 = decompose(len(a1) - 2 - v4, a1)
                v3 = v3 * v5 % a1
                v2 += v6
                v5, v6 = decompose(v4 + 1, a1)
                v3 = v3 * pow(v5, a1 - 2, a1) % a1
                v2 -= v6
            return v1 == 0
        return check(2) and check(5)
