class C1(object):

    def maxScore(self, a1):

        def gcd(a1, a2):
            while a2 != 0:
                v1 = a2
                a2 = a1 % a2
                a1 = v1
            return a1

        def lcm(a1, a2):
            v1 = gcd(a1, a2)
            return a1 // v1 * a2 if v1 != 0 else 0
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = [0] * v1
        v3 = [0] * v1
        v2[0] = a1[0]
        v3[0] = a1[0]
        for v4 in range(1, v1):
            v2[v4] = gcd(v2[v4 - 1], a1[v4])
            v3[v4] = lcm(v3[v4 - 1], a1[v4])
        v5 = [0] * v1
        v6 = [0] * v1
        v5[v1 - 1] = a1[v1 - 1]
        v6[v1 - 1] = a1[v1 - 1]
        for v4 in range(v1 - 2, -1, -1):
            v5[v4] = gcd(a1[v4], v5[v4 + 1])
            v6[v4] = lcm(a1[v4], v6[v4 + 1])
        v7 = v2[v1 - 1] * v3[v1 - 1]
        for v8 in range(v1):
            v9 = v2[v8 - 1] if v8 > 0 else 0
            v10 = v5[v8 + 1] if v8 + 1 < v1 else 0
            v11 = gcd(v9, v10)
            v12 = v3[v8 - 1] if v8 > 0 else 1
            v13 = v6[v8 + 1] if v8 + 1 < v1 else 1
            v14 = lcm(v12, v13)
            v7 = max(v7, v11 * v14)
        return v7
