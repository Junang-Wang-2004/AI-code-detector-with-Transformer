import collections

class C1(object):

    def minWindow(self, a1, a2):
        """
        """
        v1, v2 = (collections.Counter(a2), len(a2))
        v3, v4, v5 = (0, -1, -1)
        for v6, v7 in enumerate(a1):
            v2 -= v1[v7] > 0
            v1[v7] -= 1
            if v2:
                continue
            while v1[a1[v3]] < 0:
                v1[a1[v3]] += 1
                v3 += 1
            if v5 == -1 or v6 - v3 + 1 < v5 - v4 + 1:
                v4, v5 = (v3, v6)
        return a1[v4:v5 + 1]
