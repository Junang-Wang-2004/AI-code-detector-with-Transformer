import collections

class C1(object):

    def minGroups(self, a1):
        """
        """
        v1 = collections.Counter()
        for v2, v3 in a1:
            v1[v2] += 1
            v1[v3 + 1] -= 1
        v4 = v5 = 0
        for v6 in sorted(v1.keys()):
            v5 += v1[v6]
            v4 = max(v4, v5)
        return v4
