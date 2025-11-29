class C1:

    def findAnswer(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(1, v1):
            v2[a1[v4]].append(v4)
        v5 = []
        v6 = [None] * v1

        def traverse(a1):
            v1 = len(v5)
            for v2 in v2[a1]:
                traverse(v2)
            v5.append(a2[a1])
            v6[a1] = (v1, len(v5) - 1)
        traverse(0)

        def compute_radii(a1):
            v1 = '^#' + '#'.join(a1) + '#$'
            v2 = [0] * len(v1)
            v3, v4 = (0, 0)
            for v5 in range(1, len(v1) - 1):
                v6 = 2 * v3 - v5
                if v5 < v4:
                    v2[v5] = min(v4 - v5, v2[v6])
                while v1[v5 + v2[v5] + 1] == v1[v5 - v2[v5] - 1]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2
        v7 = compute_radii(v5)
        v8 = []
        for v4 in range(v1):
            v9, v10 = v6[v4]
            v11 = v9 + v10 + 2
            v12 = v10 - v9 + 1
            v8.append(v7[v11] >= v12)
        return v8
