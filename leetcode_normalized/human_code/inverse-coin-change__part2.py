class C1(object):

    def findCoins(self, a1):
        """
        """
        v1 = []
        v2 = [0] * (len(a1) + 1)
        v2[0] = 1
        for v3 in range(1, len(a1) + 1):
            if a1[v3 - 1] - v2[v3] == 1:
                v1.append(v3)
                for v4 in range(v3, len(a1) + 1):
                    v2[v4] += v2[v4 - v3]
            if a1[v3 - 1] - v2[v3]:
                return []
        return v1
