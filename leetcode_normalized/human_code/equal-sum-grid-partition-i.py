class C1(object):

    def canPartitionGrid(self, a1):
        """
        """

        def check(a1, a2, a3):
            v1 = 0
            for v2 in a1:
                v1 += sum((a3(v2, j) for v3 in a2))
                if v1 == total:
                    return True
                elif v1 > total:
                    break
            return False
        v1 = sum((sum(row) for v2 in a1))
        if v1 % 2:
            return False
        v1 //= 2
        return check(range(len(a1)), range(len(a1[0])), lambda i, j: a1[i][j]) or check(range(len(a1[0])), range(len(a1)), lambda i, j: a1[j][i])
