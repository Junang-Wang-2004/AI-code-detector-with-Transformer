class C1:

    def maxTargetNodes(self, a1, a2):

        def build_graph(a1):
            v1 = len(a1) + 1
            v2 = [[] for v3 in range(v1)]
            for v4, v5 in a1:
                v2[v4].append(v5)
                v2[v5].append(v4)
            return v2

        def max_partite(a1):
            v1 = len(a1)
            v2 = [-1] * v1
            v2[0] = 0
            v3 = 1
            v4 = 0
            v5 = [0]
            while v5:
                v6 = []
                for v7 in v5:
                    for v8 in a1[v7]:
                        if v2[v8] == -1:
                            v2[v8] = 1 ^ v2[v7]
                            if v2[v8] == 0:
                                v3 += 1
                            else:
                                v4 += 1
                            v6.append(v8)
                v5 = v6
            return max(v3, v4)

        def get_parts(a1):
            v1 = len(a1)
            v2 = [-1] * v1
            v2[0] = 0
            v3 = 1
            v4 = 0
            v5 = [0]
            while v5:
                v6 = []
                for v7 in v5:
                    for v8 in a1[v7]:
                        if v2[v8] == -1:
                            v2[v8] = 1 ^ v2[v7]
                            if v2[v8] == 0:
                                v3 += 1
                            else:
                                v4 += 1
                            v6.append(v8)
                v5 = v6
            v9 = []
            for v10 in range(v1):
                if v2[v10] == 0:
                    v9.append(v3)
                else:
                    v9.append(v4)
            return v9
        v1 = build_graph(a2)
        v2 = max_partite(v1)
        v3 = build_graph(a1)
        v4 = get_parts(v3)
        return [v2 + p for v5 in v4]
