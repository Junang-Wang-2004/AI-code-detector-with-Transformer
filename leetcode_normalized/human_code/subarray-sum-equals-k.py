import collections

class C1(object):

    def subarraySum(self, a1, a2):
        """
        """
        v1 = 0
        v2 = 0
        v3 = collections.defaultdict(int)
        v3[0] += 1
        for v4 in a1:
            v2 += v4
            v1 += v3[v2 - a2]
            v3[v2] += 1
        return v1
