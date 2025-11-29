import collections

class C1(object):

    def findSmallestInteger(self, a1, a2):
        """
        """
        v1 = collections.Counter((x % a2 for v2 in a1))
        v3 = min(((v1[i], i) for v4 in range(a2)))[1]
        return a2 * v1[v3] + v3
