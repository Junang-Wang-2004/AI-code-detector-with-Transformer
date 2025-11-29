v1 = 10 ** 9 + 7

class C1:

    def assignEdgeWeights(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1 + 1)]
        for v4, v5 in a1:
            v4 -= 1
            v5 -= 1
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = 18
        v7 = [[-1] * (v1 + 1) for v3 in range(v6)]
        v8 = [0] * (v1 + 1)

        def preorder(a1, a2, a3):
            v7[0][a1] = a2
            v8[a1] = a3
            for v1 in v2[a1]:
                if v1 != a2:
                    preorder(v1, a1, a3 + 1)
        preorder(0, -1, 0)
        for v9 in range(1, v6):
            for v10 in range(v1 + 1):
                if v7[v9 - 1][v10] != -1:
                    v7[v9][v10] = v7[v9 - 1][v7[v9 - 1][v10]]

        def lowest_common_ancestor(a1, a2):
            if v8[a1] > v8[a2]:
                a1, a2 = (a2, a1)
            v3 = v8[a2] - v8[a1]
            v4 = 0
            while v3 > 0:
                if v3 & 1:
                    a2 = v7[v4][a2]
                v3 >>= 1
                v4 += 1
            if a1 == a2:
                return a1
            for v4 in range(v6 - 1, -1, -1):
                if v7[v4][a1] != v7[v4][a2]:
                    a1 = v7[v4][a1]
                    a2 = v7[v4][a2]
            return v7[0][a1]
        v11 = []
        for v12 in a2:
            v13, v14 = (v12[0] - 1, v12[1] - 1)
            if v13 == v14:
                v11.append(0)
                continue
            v15 = lowest_common_ancestor(v13, v14)
            v16 = v8[v13] + v8[v14] - 2 * v8[v15]
            v11.append(pow(2, v16 - 1, v1))
        return v11
