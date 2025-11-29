import collections

class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        for v3 in a1:
            v2[v3] += 1
            v1 += v2[v3]
        return v1
