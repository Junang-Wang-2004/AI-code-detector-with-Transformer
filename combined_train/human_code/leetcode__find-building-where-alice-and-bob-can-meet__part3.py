class C1(object):

    def leftmostBuildingQueries(self, a1, a2):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2
        v1 = [-1] * len(a2)
        v2 = [[] for v3 in range(len(a1))]
        for v4, (v5, v6) in enumerate(a2):
            if v5 > v6:
                v5, v6 = (v6, v5)
            if v5 == v6 or a1[v5] < a1[v6]:
                v1[v4] = v6
            else:
                v2[v6].append((a1[v5], v4))
        v7 = []
        for v6 in reversed(range(len(a1))):
            while v7 and v7[-1][0] <= a1[v6]:
                v7.pop()
            v7.append((a1[v6], v6))
            for v8, v4 in v2[v6]:
                v9 = binary_search_right(0, len(v7) - 1, lambda x: v7[x][0] > v8)
                if v9 >= 0:
                    v1[v4] = v7[v9][1]
        return v1
