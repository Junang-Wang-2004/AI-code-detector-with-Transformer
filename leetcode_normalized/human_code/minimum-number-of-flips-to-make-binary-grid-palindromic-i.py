class C1(object):

    def minFlips(self, a1):
        """
        """

        def count(a1, a2, a3):
            return sum((a3(i, j) != a3(i, ~j) for v1 in range(a1) for v2 in range(a2 // 2)))
        v1, v2 = (len(a1), len(a1[0]))
        return min(count(v1, v2, lambda i, j: a1[i][j]), count(v2, v1, lambda i, j: a1[j][i]))
