class C1(object):

    def numMusicPlaylists(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = [[0] * (a1 + 1) for v3 in range(a2 + 1)]
        v2[0][0] = 1
        for v4 in range(1, a2 + 1):
            for v5 in range(1, min(v4, a1) + 1):
                v2[v4][v5] = v2[v4 - 1][v5] * max(v5 - a3, 0) % v1
                v2[v4][v5] = (v2[v4][v5] + v2[v4 - 1][v5 - 1] * v5 % v1) % v1
        return v2[a2][a1]
