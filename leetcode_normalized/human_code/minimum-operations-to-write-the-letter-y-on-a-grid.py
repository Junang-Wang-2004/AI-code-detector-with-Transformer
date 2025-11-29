class C1(object):

    def minimumOperationsToWriteY(self, a1):
        """
        """
        v1 = [[0] * 3 for v2 in range(2)]
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v1[v3 <= (len(a1[0]) - 1) // 2 and (v3 - v4 == 0 or v3 + v4 == len(a1[0]) - 1) or v3 > (len(a1[0]) - 1) // 2 == v4][a1[v3][v4]] += 1
        return len(a1) * len(a1[0]) - max((v1[0][v3] + v1[1][v4] for v3 in range(3) for v4 in range(3) if v3 != v4))
