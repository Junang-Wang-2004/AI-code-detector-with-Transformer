class C1:

    def countHighestScoreNodes(self, a1):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(1, v1):
            v2[a1[v4]].append(v4)
        v5 = [0] * v1

        def get_subtree_size(a1):
            v1 = 1
            for v2 in v2[a1]:
                v1 += get_subtree_size(v2)
            v5[a1] = v1
            return v1
        get_subtree_size(0)
        v6 = 0
        v7 = 0
        for v8 in range(v1):
            v9 = 1
            for v10 in v2[v8]:
                v9 *= v5[v10]
            v11 = v1 - v5[v8]
            v12 = max(v11, 1) * v9
            if v12 > v6:
                v6 = v12
                v7 = 1
            elif v12 == v6:
                v7 += 1
        return v7
