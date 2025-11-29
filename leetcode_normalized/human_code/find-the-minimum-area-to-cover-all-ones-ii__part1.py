class C1(object):

    def minimumSum(self, a1):
        """
        """

        def count(a1, a2):
            v1 = [[0] * len(a1[0]) for v2 in range(len(a1))]
            v3 = [len(a1)] * len(a1[0])
            v4 = [-1] * len(a1[0])
            for v5 in a1(range(len(a1))):
                v6, v7, v8, v9 = (len(a1[0]), -1, len(a1), -1)
                for v10 in a2(range(len(a1[0]))):
                    if a1[v5][v10]:
                        v3[v10] = min(v3[v10], v5)
                        v4[v10] = max(v4[v10], v5)
                    v8 = min(v8, v3[v10])
                    v9 = max(v9, v4[v10])
                    if v4[v10] >= 0:
                        v6 = min(v6, v10)
                        v7 = max(v7, v10)
                    v1[v5][v10] = (v7 - v6 + 1) * (v9 - v8 + 1) if v7 >= 0 else 0
            return v1

        def count2(a1):

            def get_n():
                return len(a1) if not a1 else len(a1[0])

            def get_m():
                return len(a1[0]) if not a1 else len(a1)

            def get(a1, a2):
                return a1[a1][a2] if not a1 else a1[a2][a1]
            v1 = [get_m() for v2 in range(get_n())]
            v3 = [-1 for v2 in range(get_n())]
            for v4 in range(get_n()):
                for v5 in range(get_m()):
                    if get(v4, v5) == 0:
                        continue
                    v1[v4] = min(v1[v4], v5)
                    v3[v4] = max(v3[v4], v5)
            v6 = [[0] * get_n() for v2 in range(get_n())]
            for v4 in range(len(v6)):
                v7, v8, v9, v10 = (get_m(), -1, get_n(), -1)
                for v5 in range(v4, len(v6[0])):
                    if v3[v5] != -1:
                        v7 = min(v7, v1[v5])
                        v8 = max(v8, v3[v5])
                        v9 = min(v9, v5)
                        v10 = max(v10, v5)
                    v6[v4][v5] = (v8 - v7 + 1) * (v10 - v9 + 1) if v8 >= 0 else 0
            return v6
        v1 = count(lambda x: x, lambda x: x)
        v2 = count(lambda x: x, reversed)
        v3 = count(reversed, lambda x: x)
        v4 = count(reversed, reversed)
        v5 = count2(False)
        v6 = count2(True)
        v7 = float('inf')
        for v8 in range(len(a1) - 1):
            for v9 in range(len(a1[0]) - 1):
                v7 = min(v7, v1[v8][v9] + v2[v8][v9 + 1] + v5[v8 + 1][len(a1) - 1], v5[0][v8] + v3[v8 + 1][v9] + v4[v8 + 1][v9 + 1], v1[v8][v9] + v3[v8 + 1][v9] + v6[v9 + 1][len(a1[0]) - 1], v6[0][v9] + v2[v8][v9 + 1] + v4[v8 + 1][v9 + 1])
        for v8 in range(len(a1) - 2):
            for v9 in range(v8 + 1, len(a1) - 1):
                v7 = min(v7, v5[0][v8] + v5[v8 + 1][v9] + v5[v9 + 1][len(a1) - 1])
        for v8 in range(len(a1[0]) - 2):
            for v9 in range(v8 + 1, len(a1[0]) - 1):
                v7 = min(v7, v6[0][v8] + v6[v8 + 1][v9] + v6[v9 + 1][len(a1[0]) - 1])
        return v7
