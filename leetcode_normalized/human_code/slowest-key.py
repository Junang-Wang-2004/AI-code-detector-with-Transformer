import collections

class C1(object):

    def slowestKey(self, a1, a2):
        """
        """
        v1, v2 = ('a', collections.Counter())
        for v3, v4 in enumerate(a2):
            v2[v4] = max(v2[v4], a1[v3] - (a1[v3 - 1] if v3 > 0 else 0))
            if v2[v4] > v2[v1] or (v2[v4] == v2[v1] and v4 > v1):
                v1 = v4
        return v1
