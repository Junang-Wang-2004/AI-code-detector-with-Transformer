class C1(object):

    def numberOfBeautifulIntegers(self, a1, a2, a3):
        """
        """

        def f(a1):
            v1 = list(map(int, str(a1)))
            v2 = [[[[0] * a3 for v3 in range(2 * len(v1) + 1)] for v3 in range(2)] for v3 in range(2)]
            for v4 in range(2):
                v2[0][v4][0][0] = 1
            for v5 in reversed(range(len(v1))):
                v6 = [[[[0] * a3 for v3 in range(2 * len(v1) + 1)] for v3 in range(2)] for v3 in range(2)]
                for v7 in range(2):
                    for v4 in range(2):
                        for v8 in range((v1[v5] if v4 else 9) + 1):
                            v9 = int(v7 and v8 == 0)
                            v10 = int(v4 and v8 == v1[v5])
                            for v11 in range(-len(v1), len(v1) + 1):
                                v12 = v11 + ((1 if v8 % 2 == 0 else -1) if v9 == 0 else 0)
                                for v13 in range(a3):
                                    v14 = (v13 * 10 + v8) % a3
                                    v6[v7][v4][v11][v13] += v2[v9][v10][v12][v14]
                v2 = v6
            return v2[1][1][0][0]
        return f(a2) - f(a1 - 1)
