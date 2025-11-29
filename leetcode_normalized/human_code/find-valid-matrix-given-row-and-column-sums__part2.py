class C1(object):

    def restoreMatrix(self, a1, a2):
        """
        """
        v1 = [[0] * len(a2) for v2 in range(len(a1))]
        for v3 in range(len(v1)):
            for v4 in range(len(v1[v3])):
                v1[v3][v4] = min(a1[v3], a2[v4])
                a1[v3] -= v1[v3][v4]
                a2[v4] -= v1[v3][v4]
        return v1
