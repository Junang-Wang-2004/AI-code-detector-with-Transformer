import collections

class C1(object):

    def beautifulSubarrays(self, a1):
        """
        """
        v1 = collections.Counter()
        v1[0] = 1
        v2 = v3 = 0
        for v4 in a1:
            v3 ^= v4
            v2 += v1[v3]
            v1[v3] += 1
        return v2
