import collections

class C1(object):

    def maximumLength(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = 0
        for v3 in v1.keys():
            if v3 == 1:
                v2 = max(v2, v1[v3] - (1 if v1[v3] % 2 == 0 else 0))
                continue
            v4 = 0
            while v3 in v1 and v1[v3] >= 2:
                v4 += 2
                v3 *= v3
            v4 += 1 if v3 in v1 else -1
            v2 = max(v2, v4)
        return v2
