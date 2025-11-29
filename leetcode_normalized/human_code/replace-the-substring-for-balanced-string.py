import collections

class C1(object):

    def balancedString(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = len(a1)
        v3 = 0
        for v4 in range(len(a1)):
            v1[a1[v4]] -= 1
            while v3 < len(a1) and all((v <= len(a1) // 4 for v5 in v1.values())):
                v2 = min(v2, v4 - v3 + 1)
                v1[a1[v3]] += 1
                v3 += 1
        return v2
