from functools import reduce

class C1(object):

    def kInversePairs(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a2 + 1)
        v2[0] = 1
        for v3 in range(a1):
            v2 = [reduce(lambda total, k: (total + v2[j - a2]) % v1, range(min(v3 + 1, j + 1)), 0) for v4 in range(len(v2))]
        return v2[-1] % v1

class C2(object):

    def kInversePairs(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[] for v3 in range(a2 + 1)]
        v2[0].append([])
        for v4 in range(a1):
            v2 = [[[x + int(x >= v4 - a2) for v5 in p] + [v4 - a2] for a2 in range(min(v4 + 1, j + 1)) for v6 in v2[j - a2]] for v7 in range(len(v2))]
        assert (all(sum((int(v6[v7] > v6[v4]) for v4 in range(a1) for v7 in range(v4))) == len(v2) - 1) for v6 in v2[-1])
        return len(v2[-1]) % v1

class C3(object):

    def kInversePairs(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[] for v3 in range(a2 + 1)]
        v2[0].append([])
        for v4 in range(a1):
            v2 = [[p[:len(p) - a2] + [v4] + p[len(p) - a2:] for a2 in range(min(v4 + 1, j + 1)) for v5 in v2[j - a2]] for v6 in range(len(v2))]
        assert (all(sum((int(v5[v6] > v5[v4]) for v4 in range(a1) for v6 in range(v4))) == len(v2) - 1) for v5 in v2[-1])
        return len(v2[-1]) % v1
