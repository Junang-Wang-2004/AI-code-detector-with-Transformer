class C1(object):

    def shortestDistanceAfterQueries(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3 in range(a1 - 1):
            v1[v3].append(v3 + 1)
        v4 = []
        v5 = float('inf')
        for v6, v7 in a2:
            v1[v6].append(v7)
            v8 = [v5] * a1
            v8[0] = 0
            for v3 in range(a1):
                for v9 in v1[v3]:
                    v8[v9] = min(v8[v9], v8[v3] + 1)
            v4.append(v8[a1 - 1])
        return v4
