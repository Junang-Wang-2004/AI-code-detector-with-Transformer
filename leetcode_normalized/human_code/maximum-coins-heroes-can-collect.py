class C1(object):

    def maximumCoins(self, a1, a2, a3):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])
        v2 = list(range(len(a2)))
        v2.sort(key=lambda x: a2[x])
        v3 = [0] * len(v1)
        v4 = v5 = 0
        for v6 in v1:
            for v4 in range(v4, len(v2)):
                if a2[v2[v4]] > a1[v6]:
                    break
                v5 += a3[v2[v4]]
            else:
                v4 = len(v2)
            v3[v6] = v5
        return v3
