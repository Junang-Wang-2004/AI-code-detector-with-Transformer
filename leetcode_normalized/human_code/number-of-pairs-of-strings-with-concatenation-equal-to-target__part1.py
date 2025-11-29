import collections

class C1(object):

    def numOfPairs(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        v2 = 0
        for v3 in a1:
            v4, v5 = (v1[-(len(a2) - len(v3))], v1[len(a2) - len(v3)])
            if a2.startswith(v3):
                v2 += v4
                v1[len(v3)] += 1
            if a2.endswith(v3):
                v2 += v5
                v1[-len(v3)] += 1
        return v2
