import itertools

class C1(object):

    def paintWalls(self, a1, a2):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2, v3 in zip(a1, a2):
            for v4 in reversed(range(1, len(a1) + 1)):
                v1[v4] = min(v1[v4], v1[max(v4 - (v3 + 1), 0)] + v2)
        return v1[-1]
