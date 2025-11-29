import collections

class C1(object):

    def findWinners(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = set()
        for v3, v4 in a1:
            v1[v4] += 1
            v2.add(v3)
            v2.add(v4)
        return [[v3 for v3 in sorted(v2) if v1[v3] == i] for v5 in range(2)]
