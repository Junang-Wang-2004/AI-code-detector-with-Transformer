class C1(object):

    def findCoins(self, a1):
        """
        """
        v1 = []
        for v2 in range(1, len(a1) + 1):
            if a1[v2 - 1] == 1:
                v1.append(v2)
                for v3 in reversed(range(v2, len(a1) + 1)):
                    a1[v3 - 1] -= a1[v3 - v2 - 1] if v3 - v2 - 1 >= 0 else 1
            if a1[v2 - 1]:
                return []
        return v1
