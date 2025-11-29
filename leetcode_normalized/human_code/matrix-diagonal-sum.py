class C1(object):

    def diagonalSum(self, a1):
        """
        """
        return sum((a1[i][i] + a1[~i][i] for v1 in range(len(a1)))) - (a1[len(a1) // 2][len(a1) // 2] if len(a1) % 2 == 1 else 0)
