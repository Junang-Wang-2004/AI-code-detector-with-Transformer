class C1(object):

    def minMaxSums(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        if v2 == 0 or a2 == 0:
            return 0
        v3 = sorted(a1)
        v4 = a2 - 1
        v5 = [0] * v2
        v5[0] = 1
        v6 = 1 if v4 == 0 else 0

        def modinv(a1):
            return pow(a1, v1 - 2, v1)
        for v7 in range(1, v2):
            v8 = v6 if v7 - 1 >= v4 else 0
            v5[v7] = (2 * v5[v7 - 1] - v8 + v1) % v1
            if v7 == v4:
                v6 = 1
            elif v7 > v4:
                v6 = v6 * (v7 * modinv(v7 - v4)) % v1
        v9 = 0
        for v7 in range(v2):
            v9 = (v9 + v3[v7] * v5[v7] % v1) % v1
            v9 = (v9 + v3[v7] * v5[v2 - 1 - v7] % v1) % v1
        return v9
