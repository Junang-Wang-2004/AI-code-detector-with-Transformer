import collections

class C1(object):

    def countTriplets(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in range(len(a1)):
            for v3 in range(len(a1)):
                v1[a1[v2] & a1[v3]] += 1
        v4 = 0
        for v5 in range(len(a1)):
            for v6 in v1:
                if a1[v5] & v6 == 0:
                    v4 += v1[v6]
        return v4
