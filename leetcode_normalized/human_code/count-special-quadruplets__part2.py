import collections

class C1(object):

    def countQuadruplets(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in range(3, len(a1)):
            for v3 in range(2, v2):
                v1[a1[v2] - a1[v3]].append(v3)
        return sum((sum((b < v3 for v3 in v1[a1[a] + a1[b]])) for v4 in range(1, len(a1) - 2) for v5 in range(v4)))
