class C1(object):

    def pathExistenceQueries(self, a1, a2, a3, a4):
        """
        """

        def ceil_log2_x(a1):
            return (a1 - 1).bit_length() if a1 - 1 >= 0 else -1
        v1 = sorted((i for v2 in range(a1)), key=lambda i: a2[v2])
        v3 = [0] * a1
        for v4, v2 in enumerate(v1):
            v3[v2] = v4
        v5 = [0] * a1
        for v2 in range(a1 - 1):
            v5[v2 + 1] = v5[v2] + int(a2[v1[v2 + 1]] - a2[v1[v2]] > a3)
        v6 = [[a1 - 1] * a1 for v7 in range(ceil_log2_x(a1 - 1) + 1)]
        v8 = 0
        for v9 in range(a1):
            while a2[v1[v9]] - a2[v1[v8]] > a3:
                v6[0][v8] = v9 - 1
                v8 += 1
        for v2 in range(len(v6) - 1):
            for v10 in range(a1):
                v6[v2 + 1][v10] = v6[v2][v6[v2][v10]]
        v11 = [-1] * len(a4)
        for v4, (v2, v10) in enumerate(a4):
            if v2 == v10:
                v11[v4] = 0
                continue
            if v5[v3[v2]] != v5[v3[v10]]:
                continue
            if v3[v2] > v3[v10]:
                v2, v10 = (v10, v2)
            v12, v13 = (v3[v2], 0)
            for v14 in reversed(range(len(v6))):
                if v6[v14][v12] < v3[v10]:
                    v12 = v6[v14][v12]
                    v13 += 1 << v14
            v11[v4] = v13 + 1
        return v11
