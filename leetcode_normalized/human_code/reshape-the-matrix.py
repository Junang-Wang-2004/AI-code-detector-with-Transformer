class C1(object):

    def matrixReshape(self, a1, a2, a3):
        """
        """
        if not a1 or a2 * a3 != len(a1) * len(a1[0]):
            return a1
        v1 = [[0 for v2 in range(a3)] for v2 in range(a2)]
        v3 = 0
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v1[v3 / a3][v3 % a3] = a1[v4][v5]
                v3 += 1
        return v1
