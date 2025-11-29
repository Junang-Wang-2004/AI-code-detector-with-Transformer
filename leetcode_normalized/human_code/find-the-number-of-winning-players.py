import collections

class C1(object):

    def winningPlayerCount(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(lambda: collections.defaultdict(int))
        for v2, v3 in a2:
            v1[v2][v3] += 1
        return sum((i < max(cnt.values()) for v4, v5 in v1.items()))
