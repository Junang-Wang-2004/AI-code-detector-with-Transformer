import collections

class C1(object):

    def maxStudentsOnBench(self, a1):
        """
        """
        v1 = collections.defaultdict(set)
        for v2, v3 in a1:
            v1[v3].add(v2)
        return max((len(x) for v4 in v1.values())) if v1 else 0
