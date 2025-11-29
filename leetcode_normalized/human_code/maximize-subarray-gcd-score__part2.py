class C1(object):

    def maxGCDScore(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lower_bit(a1):
            return a1 & -a1
        v1 = 0
        for v2 in range(len(a1)):
            v3 = float('inf')
            v4 = v5 = 0
            for v6 in range(v2, len(a1)):
                v4 = gcd(v4, a1[v6])
                v7 = lower_bit(a1[v6])
                if v7 < v3:
                    v3 = v7
                    v5 = 0
                if v7 == v3:
                    v5 += 1
                v1 = max(v1, v4 * (v6 - v2 + 1) * (2 if v5 <= a2 else 1))
                if v4 * (len(a1) - v2) * 2 <= v1:
                    break
        return v1
