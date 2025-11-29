import collections

class C1(object):

    def numWays(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0] * (len(a2) + 1) for v3 in range(2)]
        for v4 in range(len(v2)):
            v2[v4][0] = 1
        for v4 in range(len(a1[0])):
            v5 = collections.Counter((w[v4] for v6 in a1))
            for v7 in reversed(range(len(a2))):
                v2[(v4 + 1) % 2][v7 + 1] = v2[v4 % 2][v7 + 1] + v2[v4 % 2][v7] * v5[a2[v7]] % v1
        return v2[len(a1[0]) % 2][-1] % v1
