class C1(object):

    def numMusicPlaylists(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0 for v3 in range(1 + a2)] for v3 in range(2)]
        v2[0][0] = v2[1][1] = 1
        for v4 in range(1, a1 + 1):
            v2[v4 % 2][v4] = v2[(v4 - 1) % 2][v4 - 1] * v4 % v1
            for v5 in range(v4 + 1, a2 + 1):
                v2[v4 % 2][v5] = (v2[v4 % 2][v5 - 1] * max(v4 - a3, 0) % v1 + v2[(v4 - 1) % 2][v5 - 1] * v4 % v1) % v1
        return v2[a1 % 2][a2]
