import collections

class C1(object):

    def maxIncreasingCells(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                v1[a1[v2][v3]].append((v2, v3))
        v4 = [[0] * len(a1[0]) for v5 in range(len(a1))]
        v6, v7 = ([0] * len(a1), [0] * len(a1[0]))
        for v8 in sorted(v1.keys()):
            for v2, v3 in v1[v8]:
                v4[v2][v3] = max(v6[v2], v7[v3]) + 1
            for v2, v3 in v1[v8]:
                v6[v2] = max(v6[v2], v4[v2][v3])
                v7[v3] = max(v7[v3], v4[v2][v3])
        return max(v6)
