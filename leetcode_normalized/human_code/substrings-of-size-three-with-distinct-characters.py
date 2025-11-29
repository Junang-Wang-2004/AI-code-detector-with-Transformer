import collections

class C1(object):

    def countGoodSubstrings(self, a1):
        """
        """
        v1 = 3
        v2 = 0
        v3 = collections.Counter()
        for v4 in range(len(a1)):
            if v4 >= v1:
                v3[a1[v4 - v1]] -= 1
                if not v3[a1[v4 - v1]]:
                    del v3[a1[v4 - v1]]
            v3[a1[v4]] += 1
            if len(v3) == v1:
                v2 += 1
        return v2
