import collections

class C1(object):

    def brightestPosition(self, a1):
        """
        """
        v1 = collections.Counter()
        for v2, v3 in a1:
            v1[v2 - v3] += 1
            v1[v2 + v3 + 1] -= 1
        v4 = None
        v5 = v6 = 0
        for v2, v7 in sorted(v1.items()):
            v6 += v7
            if v6 > v5:
                v5, v4 = (v6, v2)
        return v4
