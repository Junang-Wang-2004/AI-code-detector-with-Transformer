class C1:

    def triangularSum(self, a1):

        def strip_factor(a1, a2):
            if a1 == 0:
                return (0, 0)
            v1 = 0
            while a1 % a2 == 0:
                a1 //= a2
                v1 += 1
            return (a1, v1)

        def pow_2_mod10(a1):
            v1 = [2, 4, 8, 6]
            return v1[(a1 - 1) % 4]

        def pow_5_mod10(a1):
            return 5

        def mod10_inv(a1):
            v1 = {1: 1, 3: 7, 7: 3, 9: 9}
            return v1[a1]
        v1 = len(a1)
        v2 = 0
        v3 = 1
        v4 = 0
        v5 = 0
        for v6 in range(v1):
            if v4 == 0 and v5 == 0:
                v7 = 1
            elif v4 > 0 and v5 == 0:
                v7 = pow_2_mod10(v4)
            elif v4 == 0 and v5 > 0:
                v7 = pow_5_mod10(v5)
            else:
                v7 = 0
            v8 = v3 * v7 % 10
            v2 = (v2 + v8 * a1[v6]) % 10
            v9, v10 = strip_factor(v1 - 1 - v6, 2)
            v4 += v10
            v9, v11 = strip_factor(v9, 5)
            v5 += v11
            v12, v10 = strip_factor(v6 + 1, 2)
            v4 -= v10
            v12, v11 = strip_factor(v12, 5)
            v5 -= v11
            v3 = v3 * (v9 % 10) % 10
            v13 = mod10_inv(v12 % 10)
            v3 = v3 * v13 % 10
        return v2
