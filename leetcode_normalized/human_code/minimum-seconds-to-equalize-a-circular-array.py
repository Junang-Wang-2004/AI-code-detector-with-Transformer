import collections

class C1(object):

    def minimumSeconds(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = collections.defaultdict(int)
        for v3 in range(2 * len(a1)):
            v4 = a1[v3 % len(a1)]
            v2[v4] = max(v2[v4], v3 - v1[v4])
            v1[v4] = v3
        return min(v2.values()) // 2
