class C1(object):

    def maxScore(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2
        v1 = [0] * (len(a1) + 1)
        v2 = [0] * (len(a1) + 1)
        v2[-1] = 1
        for v3 in reversed(range(len(a1))):
            v1[v3] = gcd(v1[v3 + 1], a1[v3])
            v2[v3] = lcm(v2[v3 + 1], a1[v3])
        v4 = v1[0] * v2[0]
        v5, v6 = (0, 1)
        for v3 in range(len(a1)):
            v4 = max(v4, gcd(v5, v1[v3 + 1]) * lcm(v6, v2[v3 + 1]))
            v5 = gcd(v5, a1[v3])
            v6 = lcm(v6, a1[v3])
        return v4
