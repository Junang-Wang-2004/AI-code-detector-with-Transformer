from functools import reduce

class C1(object):

    def numberOfPermutations(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [-1] * a1
        for v3, v4 in a2:
            v2[v3] = v4
        v5 = [1]
        v6 = 0
        for v3 in range(a1):
            if v2[v3] != -1:
                v5 = [reduce(lambda total, i: (total + v5[v3]) % v1, range(max(v2[v3] - v3 - v6, 0), min(v2[v3] + 1 - v6, len(v5))), 0)]
                v6 = v2[v3]
                continue
            v7 = [0] * min(len(v5) + (v3 + 1 - 1), v2[-1] + 1 - v6)
            for v8 in range(len(v7)):
                v7[v8] = v5[v8] if v8 < len(v5) else 0
                if v8 - 1 >= 0:
                    v7[v8] = (v7[v8] + v7[v8 - 1]) % v1
                if v8 - (v3 + 1) >= 0:
                    v7[v8] = (v7[v8] - v5[v8 - (v3 + 1)]) % v1
            v5 = v7
        return v5[-1]
