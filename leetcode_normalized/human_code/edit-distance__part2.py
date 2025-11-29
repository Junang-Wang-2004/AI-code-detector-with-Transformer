class C1(object):

    def minDistance(self, a1, a2):
        v1 = [[i] for v2 in range(len(a1) + 1)]
        v1[0] = [j for v3 in range(len(a2) + 1)]
        for v2 in range(1, len(a1) + 1):
            for v3 in range(1, len(a2) + 1):
                v4 = v1[v2][v3 - 1] + 1
                v5 = v1[v2 - 1][v3] + 1
                v6 = v1[v2 - 1][v3 - 1]
                if a1[v2 - 1] != a2[v3 - 1]:
                    v6 += 1
                v1[v2].append(min(v4, v5, v6))
        return v1[-1][-1]
