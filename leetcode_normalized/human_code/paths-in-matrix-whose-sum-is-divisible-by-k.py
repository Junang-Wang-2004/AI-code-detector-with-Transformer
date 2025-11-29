class C1(object):

    def numberOfPaths(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0 for v3 in range(a2)] for v3 in range(len(a1[0]))]
        v2[0][0] = 1
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v2[v5] = [((v2[v5 - 1][(l - a1[v4][v5]) % a2] if v5 - 1 >= 0 else 0) + v2[v5][(l - a1[v4][v5]) % a2]) % v1 for v6 in range(a2)]
        return v2[-1][0]
