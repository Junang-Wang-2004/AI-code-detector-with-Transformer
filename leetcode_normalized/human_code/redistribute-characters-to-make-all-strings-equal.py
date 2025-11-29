import collections

class C1(object):

    def makeEqual(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            for v3 in v2:
                v1[v3] += 1
        return all((v % len(a1) == 0 for v4 in v1.values()))
