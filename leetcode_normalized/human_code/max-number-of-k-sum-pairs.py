import collections

class C1(object):

    def maxOperations(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        v2 = 0
        for v3 in a1:
            if a2 - v3 in v1 and v1[a2 - v3]:
                v1[a2 - v3] -= 1
                v2 += 1
            else:
                v1[v3] += 1
        return v2
