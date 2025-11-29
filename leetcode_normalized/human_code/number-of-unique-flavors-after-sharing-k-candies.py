import collections

class C1(object):

    def shareCandies(self, a1, a2):
        """
        """
        v1 = collections.Counter((a1[i] for v2 in range(a2, len(a1))))
        v3 = v4 = len(v1)
        for v2 in range(a2, len(a1)):
            v1[a1[v2]] -= 1
            v4 += (v1[a1[v2 - a2]] == 0) - (v1[a1[v2]] == 0)
            v1[a1[v2 - a2]] += 1
            v3 = max(v3, v4)
        return v3
