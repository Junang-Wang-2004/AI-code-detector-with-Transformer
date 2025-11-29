class C1(object):

    def countPathsWithXorValue(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 16
        v3 = [[0] * v2 for v4 in range(len(a1[0]))]
        v3[0][0] = 1
        for v5 in range(len(a1)):
            v6 = [[0] * v2 for v4 in range(len(a1[0]))]
            for v7 in range(len(a1[0])):
                for v8 in range(v2):
                    v6[v7][a1[v5][v7] ^ v8] = (v3[v7][v8] + (v6[v7 - 1][v8] if v7 - 1 >= 0 else 0)) % v1
            v3 = v6
        return v3[-1][a2]
