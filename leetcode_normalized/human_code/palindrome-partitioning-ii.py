class C1(object):

    def minCut(self, a1):
        v1 = [[False for v2 in range(len(a1))] for v3 in range(len(a1))]
        v4 = [len(a1) - 1 - v3 for v3 in range(len(a1) + 1)]
        for v3 in reversed(range(len(a1))):
            for v2 in range(v3, len(a1)):
                if a1[v3] == a1[v2] and (v2 - v3 < 2 or v1[v3 + 1][v2 - 1]):
                    v1[v3][v2] = True
                    v4[v3] = min(v4[v3], v4[v2 + 1] + 1)
        return v4[0]
