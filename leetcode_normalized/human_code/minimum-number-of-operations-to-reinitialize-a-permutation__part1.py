class C1(object):

    def reinitializePermutation(self, a1):
        """
        """

        def discrete_log(a1, a2, a3):
            a1 %= a3
            a2 %= a3
            v3 = int(a3 ** 0.5) + 1
            v4 = pow(a1, v3, a3)
            v5 = {}
            v6 = a2
            for v7 in range(v3 + 1):
                v5[v6] = v7
                v6 = v6 * a1 % a3
            v6 = 1
            for v8 in range(1, v3 + 1):
                v6 = v6 * v4 % a3
                if v6 in v5:
                    return v3 * v8 - v5[v6]
            return -1
        return 1 + discrete_log(2, a1 // 2, a1 - 1)
