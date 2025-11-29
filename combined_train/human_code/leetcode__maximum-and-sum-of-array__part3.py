class C1(object):

    def maximumANDSum(self, a1, a2):
        """
        """

        def count(a1):
            v1 = 0
            while a1:
                v1 += a1 % 3
                a1 //= 3
            return v1
        v1 = [0] * 3 ** a2
        for v2 in range(1, len(v1)):
            v3 = count(v2) - 1
            v4 = a1[v3] if v3 < len(a1) else 0
            v5 = 1
            for v6 in range(1, a2 + 1):
                if v2 // v5 % 3:
                    v1[v2] = max(v1[v2], (v4 & v6) + v1[v2 - v5])
                v5 *= 3
        return v1[-1]
