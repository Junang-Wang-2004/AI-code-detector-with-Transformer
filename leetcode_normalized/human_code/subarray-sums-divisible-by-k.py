import collections

class C1(object):

    def subarraysDivByK(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        v1[0] = 1
        v2, v3 = (0, 0)
        for v4 in a1:
            v3 = (v3 + v4) % a2
            v2 += v1[v3]
            v1[v3] += 1
        return v2
