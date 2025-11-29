import collections

class C1(object):

    def countGood(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        v4 = collections.Counter()
        for v5 in range(len(a1)):
            v2 += v4[a1[v5]]
            v4[a1[v5]] += 1
            while v2 >= a2:
                v4[a1[v3]] -= 1
                v2 -= v4[a1[v3]]
                v3 += 1
            v1 += v3
        return v1
