import collections

class C1(object):

    def countKDifference(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = 0
        for v3 in a1:
            if v3 - a2 in v1:
                v2 += v1[v3 - a2]
            if v3 + a2 in v1:
                v2 += v1[v3 + a2]
            v1[v3] += 1
        return v2
