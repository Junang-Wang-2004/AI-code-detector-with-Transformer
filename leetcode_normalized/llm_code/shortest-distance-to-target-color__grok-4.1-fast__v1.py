class C1(object):

    def shortestDistanceColor(self, a1, a2):
        v1 = len(a1)
        v2 = [[-1] * v1 for v3 in range(3)]
        for v4 in range(3):
            v5 = v4 + 1
            v6 = [-1] * v1
            v7 = -1
            for v8 in range(v1):
                if a1[v8] == v5:
                    v6[v8] = v8
                    v7 = v8
                else:
                    v6[v8] = v7
            v9 = [v1] * v1
            v7 = v1
            for v8 in range(v1 - 1, -1, -1):
                if a1[v8] == v5:
                    v9[v8] = v8
                    v7 = v8
                else:
                    v9[v8] = v7
            for v8 in range(v1):
                v10 = v1
                if v6[v8] != -1:
                    v10 = min(v10, v8 - v6[v8])
                if v9[v8] != v1:
                    v10 = min(v10, v9[v8] - v8)
                if v10 < v1:
                    v2[v4][v8] = v10
        return [v2[q[1] - 1][q[0]] for v11 in a2]
