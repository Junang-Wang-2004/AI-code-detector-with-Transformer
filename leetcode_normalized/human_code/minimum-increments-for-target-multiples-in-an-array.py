class C1(object):

    def minimumIncrements(self, a1, a2):
        """
        """
        v1 = float('inf')

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2
        v2 = len(a1)
        v3 = len(a2)
        v4 = [0] * (1 << v3)
        for v5 in range(1 << v3):
            v6 = 1
            for v7 in range(v3):
                if v5 & 1 << v7:
                    v6 = lcm(v6, a2[v7])
            v4[v5] = v6
        v8 = [v1] * (1 << v3)
        v8[0] = 0
        for v9 in a1:
            for v5 in reversed(range(1 << v3)):
                if v8[v5] == v1:
                    continue
                v10 = v11 = (1 << v3) - 1 - v5
                while v10:
                    v8[v5 | v10] = min(v8[v5 | v10], v8[v5] + (v4[v10] - v9 % v4[v10] if v9 % v4[v10] else 0))
                    v10 = v10 - 1 & v11
        return v8[-1]
