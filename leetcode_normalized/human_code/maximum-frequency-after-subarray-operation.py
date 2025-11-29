import collections

class C1(object):

    def maxFrequency(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.defaultdict(int)
        for v3 in a1:
            v2[v3] = max(v2[v3], v2[a2]) + 1
            v1 = max(v1 + int(v3 == a2), v2[v3])
        return v1
