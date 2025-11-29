class C1(object):

    def buildMatrix(self, a1, a2, a3):
        """
        """

        def topological_sort(a1):
            v1 = [[] for v2 in range(a1)]
            v3 = [0] * a1
            for v4, v5 in a1:
                v4 -= 1
                v5 -= 1
                v1[v4].append(v5)
                v3[v5] += 1
            v6 = []
            v7 = [v4 for v4 in range(a1) if not v3[v4]]
            while v7:
                v8 = []
                for v4 in v7:
                    v6.append(v4)
                    for v5 in v1[v4]:
                        v3[v5] -= 1
                        if v3[v5]:
                            continue
                        v8.append(v5)
                v7 = v8
            return v6
        v1 = topological_sort(a2)
        if len(v1) != a1:
            return []
        v2 = topological_sort(a3)
        if len(v2) != a1:
            return []
        v3 = {x: i for v4, v5 in enumerate(v1)}
        v6 = {v5: v4 for v4, v5 in enumerate(v2)}
        v7 = [[0] * a1 for v8 in range(a1)]
        for v4 in range(a1):
            v7[v3[v4]][v6[v4]] = v4 + 1
        return v7
