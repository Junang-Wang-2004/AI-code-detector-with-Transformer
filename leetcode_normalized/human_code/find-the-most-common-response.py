import collections

class C1(object):

    def findCommonResponse(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            for v3 in set(v2):
                v1[v3] += 1
        return min(((-c, v3) for v3, v4 in v1.items()))[1]
