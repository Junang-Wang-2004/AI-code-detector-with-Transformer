import collections

class C1(object):

    def numSplits(self, a1):
        """
        """
        v1, v2 = (collections.Counter(), collections.Counter(a1))
        v3 = 0
        for v4 in a1:
            v1[v4] += 1
            v2[v4] -= 1
            if not v2[v4]:
                del v2[v4]
            if len(v1) == len(v2):
                v3 += 1
        return v3
