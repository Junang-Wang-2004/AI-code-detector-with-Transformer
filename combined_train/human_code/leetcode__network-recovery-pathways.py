class C1(object):

    def findMaxPathScore(self, a1, a2, a3):
        """
        """
        v1 = float('inf')

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def topological_sort():
            v1 = [0] * len(adj)
            for v2 in range(len(adj)):
                for v3, v4 in adj[v2]:
                    v1[v3] += 1
            v5 = []
            v6 = [v2 for v2 in range(len(adj)) if not v1[v2]]
            while v6:
                v7 = []
                for v2 in v6:
                    v5.append(v2)
                    for v3, v4 in adj[v2]:
                        v1[v3] -= 1
                        if v1[v3]:
                            continue
                        v7.append(v3)
                v6 = v7
            return v5

        def check(a1):
            v1 = [v1] * len(adj)
            v1[0] = 0
            for v2 in order:
                if v1[v2] == v1:
                    continue
                for v3, v4 in adj[v2]:
                    if not (v4 >= a1 and a2[v3]):
                        continue
                    v1[v3] = min(v1[v3], v1[v2] + v4)
            return v1[-1] <= a3
        v2 = [[] for v3 in range(len(a2))]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
        v7 = topological_sort()
        v8, v9 = (v1, 0)
        for v4 in range(len(v2)):
            for v3, v6 in v2[v4]:
                v8 = min(v8, v6)
                v9 = max(v9, v6)
        v10 = binary_search_right(v8, v9, check)
        return v10 if v10 >= v8 else -1
