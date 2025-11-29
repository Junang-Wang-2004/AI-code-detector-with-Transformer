class C1:

    def partition(self, a1):
        v1 = len(a1)
        v2 = [[False] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            v2[v4][v4] = True
        for v4 in range(v1 - 1):
            if a1[v4] == a1[v4 + 1]:
                v2[v4][v4 + 1] = True
        for v5 in range(3, v1 + 1):
            for v4 in range(v1 - v5 + 1):
                v6 = v4 + v5 - 1
                if a1[v4] == a1[v6] and v2[v4 + 1][v6 - 1]:
                    v2[v4][v6] = True
        v7 = [None] * (v1 + 1)

        def find_partitions(a1):
            if a1 == v1:
                return [[]]
            if v7[a1] is not None:
                return v7[a1]
            v1 = []
            for v2 in range(a1, v1):
                if v2[a1][v2]:
                    v3 = find_partitions(v2 + 1)
                    for v4 in v3:
                        v1.append([a1[a1:v2 + 1]] + v4)
            v7[a1] = v1
            return v1
        return find_partitions(0)
