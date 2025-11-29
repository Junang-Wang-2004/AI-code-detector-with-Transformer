class C1:

    def maxOperations(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + (a1[v3] == '1')
        v4 = 0
        for v3 in range(v1 - 1):
            if a1[v3] == '1' and a1[v3 + 1] == '0':
                v4 += v2[v3 + 1]
        return v4
