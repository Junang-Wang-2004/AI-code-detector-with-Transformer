import collections

class C1(object):

    def maximalNetworkRank(self, a1, a2):
        """
        """
        v1 = [0] * a1
        v2 = collections.defaultdict(set)
        for v3, v4 in a2:
            v1[v3] += 1
            v1[v4] += 1
            v2[v3].add(v4)
            v2[v4].add(v3)
        v5 = 0
        for v6 in range(a1 - 1):
            for v7 in range(v6 + 1, a1):
                v5 = max(v5, v1[v6] + v1[v7] - int(v6 in v2 and v7 in v2[v6]))
        return v5
