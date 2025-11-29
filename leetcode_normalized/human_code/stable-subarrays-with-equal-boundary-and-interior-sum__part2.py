import collections

class C1(object):

    def countStableSubarrays(self, a1):
        """
        """
        v1 = collections.defaultdict(lambda: collections.defaultdict(int))
        v2 = v3 = 0
        for v4, v5 in enumerate(a1):
            v2 += v1[v5][v3 - v5]
            v3 += v5
            v1[v5][v3] += 1
            if v5 == 0 and v4 - 1 >= 0 and (a1[v4 - 1] == 0):
                v2 -= 1
        return v2
