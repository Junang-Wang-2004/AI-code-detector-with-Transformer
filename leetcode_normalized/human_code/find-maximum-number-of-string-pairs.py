import collections

class C1(object):

    def maximumNumberOfStringPairs(self, a1):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        for v3 in a1:
            v1 += v2[v3[::-1]]
            v2[v3] += 1
        return v1
