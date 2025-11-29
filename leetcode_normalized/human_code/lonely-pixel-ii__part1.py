import collections

class C1(object):

    def findBlackPixel(self, a1, a2):
        """
        """
        v1, v2 = ([0] * len(a1), [0] * len(a1[0]))
        v3 = collections.defaultdict(int)
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                if a1[v4][v5] == 'B':
                    v1[v4] += 1
                    v2[v5] += 1
            v3[tuple(a1[v4])] += 1
        v6 = 0
        for v4 in range(len(a1)):
            if v1[v4] == a2 and v3[tuple(a1[v4])] == a2:
                for v5 in range(len(a1[0])):
                    v6 += a1[v4][v5] == 'B' and v2[v5] == a2
        return v6
