class C1(object):

    def constructProductMatrix(self, a1):
        """
        """
        v1 = 12345
        v2 = [1] * (len(a1) * len(a1[0]) + 1)
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v2[v3 * len(a1[0]) + v4 + 1] = v2[v3 * len(a1[0]) + v4] * a1[v3][v4] % v1
        v5 = [1] * (len(a1) * len(a1[0]) + 1)
        for v3 in reversed(range(len(a1))):
            for v4 in reversed(range(len(a1[0]))):
                v5[v3 * len(a1[0]) + v4] = v5[v3 * len(a1[0]) + v4 + 1] * a1[v3][v4] % v1
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                a1[v3][v4] = v2[v3 * len(a1[0]) + v4] * v5[v3 * len(a1[0]) + v4 + 1] % v1
        return a1
