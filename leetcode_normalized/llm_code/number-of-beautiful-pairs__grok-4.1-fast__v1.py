class C1(object):

    def countBeautifulPairs(self, a1):

        def gcd(a1, a2):
            if a2 == 0:
                return a1
            return gcd(a2, a1 % a2)
        v1 = [0] * 10
        v2 = 0
        for v3 in a1:
            v4 = str(v3)
            v5 = int(v4[0])
            v6 = int(v4[-1])
            for v7 in range(1, 10):
                if gcd(v7, v6) == 1:
                    v2 += v1[v7]
            v1[v5] += 1
        return v2
