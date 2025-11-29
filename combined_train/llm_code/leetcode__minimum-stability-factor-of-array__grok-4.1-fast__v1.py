from math import gcd

class C1:

    def minStable(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = v1.bit_length()
        v3 = [[0] * v1 for v4 in range(v2)]
        for v5 in range(v1):
            v3[0][v5] = a1[v5]
        for v6 in range(1, v2):
            v7 = 1 << v6 - 1
            for v8 in range(v1 - (1 << v6) + 1):
                v3[v6][v8] = gcd(v3[v6 - 1][v8], v3[v6 - 1][v8 + v7])

        def get_gcd(a1, a2):
            v1 = a2 - a1 + 1
            v2 = v1.bit_length() - 1
            v3 = 1 << v2
            return gcd(v3[v2][a1], v3[v2][a2 - v3 + 1])

        def valid_length(a1):
            v1 = 0
            v2 = 0
            while v2 + a1 <= v1:
                if get_gcd(v2, v2 + a1 - 1) >= 2:
                    v1 += 1
                    v2 += a1
                else:
                    v2 += 1
            return v1 > a2
        v9, v10 = (0, v1)
        while v9 < v10:
            v11 = (v9 + v10 + 1) // 2
            if valid_length(v11):
                v9 = v11
            else:
                v10 = v11 - 1
        return v9
