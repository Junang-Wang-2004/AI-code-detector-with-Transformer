import collections

class C1(object):

    def maxFrequency(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        v3 = defaultdict(int)
        for v2 in a1:
            v3[v2] += 0
            v3[v2 - a2] += 1
            v3[v2 + a2 + 1] -= 1
        v4 = v5 = 0
        for v2, v6 in sorted(v3.items()):
            v5 += v6
            v4 = max(v4, v1[v2] + min(v5 - v1[v2], a3))
        return v4
