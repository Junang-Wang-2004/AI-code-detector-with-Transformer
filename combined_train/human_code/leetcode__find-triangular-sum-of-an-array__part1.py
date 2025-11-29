class C1(object):

    def triangularSum(self, a1):
        """
        """

        def exp_mod(a1, a2):
            v1 = [a1]
            while v1[-1] * a1 % a2 != v1[0]:
                v1.append(v1[-1] * a1 % a2)
            return [v1[-1]] + v1[:-1]

        def inv_mod(a1, a2):
            v1 = a1
            while v1 * a1 % a2 != 1:
                v1 = v1 * a1 % a2
            return v1

        def factor_p(a1, a2, a3, a4):
            if a1 == 0:
                return (a1, a3)
            while a1 % a2 == 0:
                a1 //= a2
                a3 += a4
            return (a1, a3)
        v1 = {p: exp_mod(p, 10) for v2 in (2, 5)}
        v3 = {i: inv_mod(i, 10) for v4 in range(1, 10) if v4 % 2 and v4 % 5}
        v5 = 0
        v6 = 1
        v7 = {2: 0, 5: 0}
        for v4 in range(len(a1)):
            if not v7[2] and (not v7[5]):
                v5 = (v5 + v6 * a1[v4]) % 10
            elif v7[2] and (not v7[5]):
                v5 = (v5 + v6 * v1[2][v7[2] % len(v1[2])] * a1[v4]) % 10
            elif not v7[2] and v7[5]:
                v5 = (v5 + v6 * v1[5][v7[5] % len(v1[5])] * a1[v4]) % 10
            v8, v7[2] = factor_p(len(a1) - 1 - v4, 2, v7[2], 1)
            v8, v7[5] = factor_p(v8, 5, v7[5], 1)
            v9, v7[2] = factor_p(v4 + 1, 2, v7[2], -1)
            v9, v7[5] = factor_p(v9, 5, v7[5], -1)
            v6 = v6 * v8 % 10
            v6 = v6 * v3[v9 % 10] % 10
        return v5
