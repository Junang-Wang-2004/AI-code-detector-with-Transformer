class C1(object):

    def restoreMatrix(self, a1, a2):
        """
        """
        v1 = [[0] * len(a2) for v2 in range(len(a1))]
        v3 = v4 = 0
        while v3 < len(v1) and v4 < len(v1[0]):
            v1[v3][v4] = min(a1[v3], a2[v4])
            a1[v3] -= v1[v3][v4]
            a2[v4] -= v1[v3][v4]
            if not a1[v3]:
                v3 += 1
            if not a2[v4]:
                v4 += 1
        return v1
