import collections

class C1(object):

    def countStableSubarrays(self, a1):
        """
        """
        v1 = 3
        v2 = collections.defaultdict(lambda: collections.defaultdict(int))
        v3 = v4 = v5 = 0
        for v6 in range(len(a1)):
            v3 += v2[a1[v6]][v4 - a1[v6]]
            v4 += a1[v6]
            if v6 + 1 - v1 + 1 >= 0:
                v5 += a1[v6 + 1 - v1 + 1]
                v2[a1[v6 + 1 - v1 + 1]][v5] += 1
        return v3
