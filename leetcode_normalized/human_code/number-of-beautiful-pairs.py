class C1(object):

    def countBeautifulPairs(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = 0
        v2 = [0] * 10
        for v3 in a1:
            for v4 in range(1, 10):
                if gcd(v4, v3 % 10) == 1:
                    v1 += v2[v4]
            while v3 >= 10:
                v3 //= 10
            v2[v3] += 1
        return v1
