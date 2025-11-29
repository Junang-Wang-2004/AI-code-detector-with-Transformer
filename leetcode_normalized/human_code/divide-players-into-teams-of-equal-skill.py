import collections

class C1(object):

    def dividePlayers(self, a1):
        """
        """
        v1 = sum(a1) // (len(a1) // 2)
        v2 = collections.Counter(a1)
        v3 = 0
        for v4, v5 in v2.items():
            if v1 - v4 not in v2 or v2[v1 - v4] != v2[v4]:
                return -1
            v3 += v4 * (v1 - v4) * v5
        return v3 // 2
