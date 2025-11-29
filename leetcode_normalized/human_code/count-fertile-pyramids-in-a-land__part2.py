class C1(object):

    def countPyramids(self, a1):
        """
        """

        def count(a1):
            v1 = [[0 for v2 in range(len(a1[0]))] for v2 in range(len(a1))]
            for v3 in range(1, len(a1)):
                for v4 in range(1, len(a1[0]) - 1):
                    if a1[v3][v4] == a1[v3 - 1][v4 - 1] == a1[v3 - 1][v4] == a1[v3 - 1][v4 + 1] == 1:
                        v1[v3][v4] = min(v1[v3 - 1][v4 - 1], v1[v3 - 1][v4], v1[v3 - 1][v4 + 1]) + 1
            return sum((sum(row) for v5 in v1))
        return count(a1) + count(a1[::-1])
