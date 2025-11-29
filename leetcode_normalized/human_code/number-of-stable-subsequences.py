class C1(object):

    def countStableSubsequences(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0] * 2 for v3 in range(2)]
        for v4 in a1:
            v5 = v4 % 2
            v2[v5][1] = (v2[v5][1] + v2[v5][0]) % v1
            v2[v5][0] = (v2[v5][0] + 1 + v2[1 ^ v5][0] + v2[1 ^ v5][1]) % v1
        return sum((v2[v5][i] for v5 in range(2) for v6 in range(2))) % v1
