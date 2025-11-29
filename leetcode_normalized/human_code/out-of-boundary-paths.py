class C1(object):

    def findPaths(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = 1000000000 + 7
        v2 = [[[0 for v3 in range(a2)] for v3 in range(a1)] for v3 in range(2)]
        for v4 in range(a3):
            for v5 in range(a1):
                for v6 in range(a2):
                    v2[(v4 + 1) % 2][v5][v6] = (((1 if v5 == 0 else v2[v4 % 2][v5 - 1][v6]) + (1 if v5 == a1 - 1 else v2[v4 % 2][v5 + 1][v6])) % v1 + ((1 if v6 == 0 else v2[v4 % 2][v5][v6 - 1]) + (1 if v6 == a2 - 1 else v2[v4 % 2][v5][v6 + 1])) % v1) % v1
        return v2[a3 % 2][a4][a5]
