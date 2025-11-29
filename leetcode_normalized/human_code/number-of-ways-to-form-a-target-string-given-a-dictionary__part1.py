import collections

class C1(object):

    def numWays(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (len(a2) + 1)
        v2[0] = 1
        for v3 in range(len(a1[0])):
            v4 = collections.Counter((w[v3] for v5 in a1))
            for v6 in reversed(range(len(a2))):
                v2[v6 + 1] += v2[v6] * v4[a2[v6]] % v1
        return v2[-1] % v1
