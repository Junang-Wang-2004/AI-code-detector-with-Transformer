class C1(object):

    def numberOfBeautifulIntegers(self, a1, a2, a3):
        """
        """
        v1, v2, v3 = list(range(3))

        def f(a1):
            v1 = list(map(int, str(a1)))
            v2 = [[[0] * a3 for v3 in range(2 * len(v1) + 1)] for v3 in range(3)]
            for v4 in range(2):
                for v5 in (v1, v2):
                    v2[v5][0][0] = 1
            for v6 in reversed(range(len(v1))):
                v7 = [[[0] * a3 for v3 in range(2 * len(v1) + 1)] for v3 in range(3)]
                for v5 in (v1, v2, v3):
                    v7[v5][0][0] = int(v6 != 0)
                    for v8 in range(1 if v6 == 0 else 0, 10):
                        v9 = v5
                        if v5 == v1 and v8 != v1[v6]:
                            v9 = v2 if v8 < v1[v6] else v3
                        for v10 in range(-len(v1), len(v1) + 1):
                            v11 = v10 + (1 if v8 % 2 == 0 else -1)
                            for v12 in range(a3):
                                v13 = (v12 * 10 + v8) % a3
                                v7[v5][v10][v12] += v2[v9][v11][v13]
                v2 = v7
            return v2[v1][0][0]
        return f(a2) - f(a1 - 1)
