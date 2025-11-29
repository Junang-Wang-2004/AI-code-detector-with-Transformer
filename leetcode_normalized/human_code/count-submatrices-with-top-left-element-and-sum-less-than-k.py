class C1(object):

    def countSubmatrices(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if v2 - 1 >= 0:
                    a1[v2][v3] += a1[v2 - 1][v3]
                if v3 - 1 >= 0:
                    a1[v2][v3] += a1[v2][v3 - 1]
                if v2 - 1 >= 0 and v3 - 1 >= 0:
                    a1[v2][v3] -= a1[v2 - 1][v3 - 1]
                if a1[v2][v3] <= a2:
                    v1 += 1
        return v1
