class C1(object):

    def minNumberOfPrimes(self, a1, a2):
        """
        """
        v1 = [True] * (a1 + 1)
        v2 = 0
        v3 = [float('inf')] * (a1 + 1)
        v3[0] = 0
        for v4 in range(2, a1 + 1):
            if not v1[v4]:
                continue
            for v5 in range(v4 + v4, a1 + 1, v4):
                v1[v5] = False
            for v5 in range(v4, a1 + 1):
                v3[v5] = min(v3[v5], v3[v5 - v4] + 1)
            v2 += 1
            if v2 == a2:
                break
        return v3[a1] if v3[a1] != float('inf') else -1
