import collections

class C1(object):

    def numOfPairs(self, a1, a2):
        """
        """
        v1, v2 = (collections.Counter(), collections.Counter())
        v3 = 0
        for v4 in a1:
            if a2.startswith(v4):
                v3 += v2[len(a2) - len(v4)]
            if a2.endswith(v4):
                v3 += v1[len(a2) - len(v4)]
            if a2.startswith(v4):
                v1[len(v4)] += 1
            if a2.endswith(v4):
                v2[len(v4)] += 1
        return v3
