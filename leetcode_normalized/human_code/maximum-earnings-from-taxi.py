class C1(object):

    def maxTaxiEarnings(self, a1, a2):
        """
        """
        a2.sort()
        v1 = [0] * (a1 + 1)
        v2 = 0
        for v3 in range(1, a1 + 1):
            v1[v3] = max(v1[v3], v1[v3 - 1])
            while v2 < len(a2) and a2[v2][0] == v3:
                v1[a2[v2][1]] = max(v1[a2[v2][1]], v1[v3] + a2[v2][1] - a2[v2][0] + a2[v2][2])
                v2 += 1
        return v1[-1]
