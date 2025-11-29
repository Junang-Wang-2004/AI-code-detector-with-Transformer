class C1(object):

    def countNoZeroPairs(self, a1):
        """
        """
        v1 = [[[0] * 2 for v2 in range(2)] for v2 in range(2)]
        v1[0][0][0] = 1
        v3 = 1
        while a1:
            a1, v5 = divmod(a1, 10)
            v6 = [[[0] * 2 for v2 in range(2)] for v2 in range(2)]
            for v7 in range(2):
                for v8 in range(2):
                    for v9 in range(2):
                        if not v1[v7][v8][v9]:
                            continue
                        for v10 in range(v3, (9 if not v8 else 0) + 1):
                            for v11 in range(v3, (9 if not v9 else 0) + 1):
                                if (v7 + v10 + v11) % 10 != v5:
                                    continue
                                v6[(v7 + v10 + v11) // 10][v8 or not v10][v9 or not v11] += v1[v7][v8][v9]
            v3 = 0
            v1 = v6
        return sum((v1[0][v8][v9] for v8 in range(2) for v9 in range(2)))
