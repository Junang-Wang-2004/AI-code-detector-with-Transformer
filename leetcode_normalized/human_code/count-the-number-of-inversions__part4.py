from functools import reduce

class C1(object):

    def numberOfPermutations(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [-1] * a1
        for v3, v4 in a2:
            v2[v3] = v4
        v5 = [0] * (v2[-1] + 1)
        v5[0] = 1
        for v3 in range(a1):
            v5 = [reduce(lambda total, k: (total + v5[j - k]) % v1, range(min(v3 + 1, j + 1)), 0) if v2[v3] == -1 or v2[v3] == j else 0 for v6 in range(len(v5))]
        return v5[-1] % v1

class C2(object):

    def numberOfPermutations(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [-1] * a1
        for v3, v4 in a2:
            v2[v3] = v4
        v5 = [[] for v6 in range(v2[-1] + 1)]
        v5[0].append([])
        for v3 in range(a1):
            v5 = [[[x + int(x >= v3 - k) for v7 in p] + [v3 - k] for v8 in range(min(v3 + 1, j + 1)) for v9 in v5[j - v8]] if v2[v3] == -1 or v2[v3] == j else [] for v10 in range(len(v5))]
        for v9 in v5[-1]:
            v11 = 0
            for v3 in range(a1):
                for v10 in range(v3):
                    v11 += int(v9[v10] > v9[v3])
                if v2[v3] != -1:
                    assert v2[v3] == v11
        return len(v5[-1]) % v1
