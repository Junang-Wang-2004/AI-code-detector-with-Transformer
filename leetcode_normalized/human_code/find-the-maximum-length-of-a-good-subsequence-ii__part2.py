import collections

class C1(object):

    def maximumLength(self, a1, a2):
        """
        """
        v1 = [collections.defaultdict(int) for v2 in range(a2 + 1)]
        v3 = [0] * (a2 + 1)
        for v4 in a1:
            for v5 in reversed(range(a2 + 1)):
                v1[v5][v4] = max(v1[v5][v4], v3[v5 - 1] if v5 - 1 >= 0 else 0) + 1
                v3[v5] = max(v3[v5], v1[v5][v4])
        return v3[a2]
