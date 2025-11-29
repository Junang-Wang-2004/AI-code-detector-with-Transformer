import collections

class C1(object):

    def numTilePossibilities(self, a1):
        """
        """
        v1 = [0.0] * (len(a1) + 1)
        v1[0] = 1.0
        for v2 in range(1, len(a1) + 1):
            v1[v2] = v1[v2 - 1] * v2
        v3 = collections.Counter(a1)
        v4 = [0.0] * (len(a1) + 1)
        v4[0] = 1.0
        for v2 in v3.values():
            v5 = [0.0] * (len(a1) + 1)
            for v6 in range(len(v4)):
                for v7 in range(v2 + 1):
                    if v7 + v6 >= len(v5):
                        break
                    v5[v6 + v7] += v4[v6] * 1.0 / v1[v7]
            v4 = v5
        v8 = 0
        for v2 in range(1, len(v4)):
            v8 += int(round(v4[v2] * v1[v2]))
        return v8
