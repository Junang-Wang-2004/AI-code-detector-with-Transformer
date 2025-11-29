import collections

class C1(object):

    def countPoints(self, a1):
        """
        """
        v1 = {'R': 1, 'G': 2, 'B': 4}
        v2 = collections.defaultdict(int)
        for v3 in range(0, len(a1), 2):
            v2[int(a1[v3 + 1])] |= v1[a1[v3]]
        return sum((x == 7 for v4 in v2.values()))
