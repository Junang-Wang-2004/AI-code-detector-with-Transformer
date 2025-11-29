import collections

class C1:

    def countKDifference(self, a1, a2):
        v1 = collections.Counter(a1)
        v2 = 0
        for v3 in v1:
            v2 += v1[v3] * v1[v3 + a2]
        return v2
