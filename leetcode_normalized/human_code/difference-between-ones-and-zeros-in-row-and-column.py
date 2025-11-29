class C1(object):

    def onesMinusZeros(self, a1):
        """
        """
        v1 = [sum((a1[i][j] for v2 in range(len(a1[0])))) for v3 in range(len(a1))]
        v4 = [sum((a1[v3][v2] for v3 in range(len(a1)))) for v2 in range(len(a1[0]))]
        return [[v1[v3] + v4[v2] - (len(a1) - v1[v3]) - (len(a1[0]) - v4[v2]) for v2 in range(len(a1[0]))] for v3 in range(len(a1))]
