import collections

class C1(object):

    def findLHS(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = 0
        for v3 in a1:
            v1[v3] += 1
            for v4 in [-1, 1]:
                if v3 + v4 in v1:
                    v2 = max(v2, v1[v3] + v1[v3 + v4])
        return v2
