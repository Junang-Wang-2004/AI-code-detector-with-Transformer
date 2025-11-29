class C1:

    def lastMarkedNodes(self, a1):
        v1 = len(a1) + 1
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [[(0, i), (0, i)] for v7 in range(v1)]

        def first_pass(a1, a2):
            for v1 in v2[a1]:
                if v1 == a2:
                    continue
                first_pass(v1, a1)
                v2, v3 = v6[v1][0]
                v4 = (v2 + 1, v3)
                if v4 > v6[a1][0]:
                    v6[a1][1] = v6[a1][0]
                    v6[a1][0] = v4
                elif v4 > v6[a1][1]:
                    v6[a1][1] = v4
        first_pass(0, -1)
        v8 = [0] * v1

        def second_pass(a1, a2, a3):
            v1, v2 = v6[a1][0]
            v3, v2 = a3
            v8[a1] = v6[a1][0][1] if v1 >= v3 else a3[1]
            for v4 in v2[a1]:
                if v4 == a2:
                    continue
                v5 = 1 if v6[a1][0][1] == v6[v4][0][1] else 0
                v6 = v6[a1][v5]
                v7 = v6 if v6 > a3 else a3
                v8 = (v7[0] + 1, v7[1])
                second_pass(v4, a1, v8)
        second_pass(0, -1, (0, -1))
        return v8
