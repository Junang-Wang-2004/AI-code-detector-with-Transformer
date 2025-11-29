class C1(object):

    def findRotation(self, a1, a2):
        """
        """
        v1 = [lambda i, j: a1[i][j] == a2[i][j], lambda i, j: a1[i][j] == a2[j][-1 - i], lambda i, j: a1[i][j] == a2[-1 - i][-1 - j], lambda i, j: a1[i][j] == a2[-1 - j][i]]
        v2 = lambda check: all((check(i, j) for v3 in range(len(a1)) for v4 in range(len(a1[0]))))
        return any((v2(check) for v5 in v1))
