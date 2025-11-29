class C1(object):

    def canPartitionGrid(self, a1):
        """
        """

        def check(a1, a2, a3):
            v1 = 0
            v2 = set()
            v3 = -1
            for v4 in a1:
                if v3 == -1:
                    v3 = v4
                for v5 in a2:
                    v1 += a3(v4, v5)
                    v2.add(a3(v4, v5))
                v6 = v1 - (total - v1)
                if v6 == 0:
                    return True
                if v4 != v3 and v5 != 0:
                    if v6 in v2:
                        return True
                elif v4 == v3:
                    if v6 in [a3(v3, 0), a3(v3, v5)]:
                        return True
                elif v6 in [a3(v3, 0), a3(v4, 0)]:
                    return True
            return False
        v1 = sum((sum(row) for v2 in a1))
        return check(range(len(a1)), range(len(a1[0])), lambda i, j: a1[i][j]) or check(reversed(range(len(a1))), range(len(a1[0])), lambda i, j: a1[i][j]) or check(range(len(a1[0])), range(len(a1)), lambda i, j: a1[j][i]) or check(reversed(range(len(a1[0]))), range(len(a1)), lambda i, j: a1[j][i])
