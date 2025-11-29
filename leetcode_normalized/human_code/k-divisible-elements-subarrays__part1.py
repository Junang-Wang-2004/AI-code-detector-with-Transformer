import collections

class C1(object):

    def countDistinct(self, a1, a2, a3):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v3 = 0
        for v4 in range(len(a1)):
            v5 = 0
            v6 = v2
            for v7 in range(v4, len(a1)):
                v5 += a1[v7] % a3 == 0
                if v5 > a2:
                    break
                if a1[v7] not in v6:
                    v3 += 1
                v6 = v6[a1[v7]]
        return v3
