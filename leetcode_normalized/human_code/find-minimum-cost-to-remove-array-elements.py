import collections

class C1(object):

    def minCost(self, a1):
        """
        """
        v1 = collections.defaultdict(lambda: float('inf'))
        v1[a1[0]] = 0
        for v2 in range(1, len(a1) - 1, 2):
            v3 = collections.defaultdict(lambda: float('inf'))
            v4, v5 = (a1[v2], a1[v2 + 1])
            for v6, v7 in v1.items():
                v8 = sorted([v4, v5, v6])
                v3[v8[0]] = min(v3[v8[0]], v7 + v8[2])
                v3[v8[2]] = min(v3[v8[2]], v7 + v8[1])
            v1 = v3
        v9 = a1[-1] if len(a1) % 2 == 0 else 0
        return min((v7 + max(v4, v9) for v4, v7 in v1.items()))
