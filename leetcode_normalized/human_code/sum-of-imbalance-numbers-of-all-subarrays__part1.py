class C1(object):

    def sumImbalanceNumbers(self, a1):
        """
        """
        v1 = [len(a1)] * len(a1)
        v2 = [len(a1)] * (len(a1) + 1 + 1)
        for v3 in reversed(range(len(a1))):
            v1[v3] = min(v2[a1[v3]], v2[a1[v3] + 1])
            v2[a1[v3]] = v3
        v4 = v5 = 0
        v2 = [-1] * (len(a1) + 1 + 1)
        for v3 in range(len(a1)):
            v5 = v2[a1[v3] + 1]
            v2[a1[v3]] = v3
            v4 += (v3 - v5) * (v1[v3] - v3)
        return v4 - (len(a1) + 1) * len(a1) // 2
