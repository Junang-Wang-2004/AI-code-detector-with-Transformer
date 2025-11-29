class C1:

    def sumOfDistancesInTree(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        v6 = [0] * a1

        def build_tree(a1, a2):
            v5[a1] = 1
            v6[a1] = 0
            for v1 in v1[a1]:
                if v1 != a2:
                    build_tree(v1, a1)
                    v5[a1] += v5[v1]
                    v6[a1] += v6[v1] + v5[v1]
        build_tree(0, -1)
        v7 = [0] * a1
        v7[0] = v6[0]

        def adjust(a1, a2):
            for v1 in v1[a1]:
                if v1 != a2:
                    v7[v1] = v7[a1] + (a1 - 2 * v5[v1])
                    adjust(v1, a1)
        adjust(0, -1)
        return v7
