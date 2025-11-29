import collections

class C1(object):

    def maxNumberOfBalloons(self, a1):
        """
        """
        v1 = 'balloon'
        v2 = collections.Counter(a1)
        v3 = collections.Counter(v1)
        return min((v2[c] // v3[c] for v4 in v3.keys()))
