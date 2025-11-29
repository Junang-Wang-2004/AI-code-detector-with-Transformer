import collections

class C1(object):

    def maxFrequency(self, a1, a2, a3):
        """
        """
        a1.sort()
        v1 = 0
        v2, v3 = (0, -1)
        v4 = collections.defaultdict(int)
        for v5 in range(len(a1)):
            while v3 + 1 < len(a1) and a1[v3 + 1] - a1[v5] <= a2:
                v4[a1[v3 + 1]] += 1
                v3 += 1
            while a1[v5] - a1[v2] > a2:
                v4[a1[v2]] -= 1
                v2 += 1
            v1 = max(v1, v4[a1[v5]] + min(v3 - v2 + 1 - v4[a1[v5]], a3))
        v2 = 0
        for v3 in range(len(a1)):
            while a1[v2] + a2 < a1[v3] - a2:
                v2 += 1
            v1 = max(v1, min(v3 - v2 + 1, a3))
        return v1
