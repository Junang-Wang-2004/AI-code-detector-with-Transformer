import collections
from functools import reduce

class C1(object):

    def sumOfPowers(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = [[collections.defaultdict(int) for v3 in range(len(a1) + 1)] for v3 in range(len(a1))]
        for v4 in range(len(a1)):
            for v5 in range(max(a2 - (len(a1) - v4 + 1) - 1, 0), v4):
                v6 = a1[v4] - a1[v5]
                v2[v4][2][v6] += 1
                for v7 in range(max(a2 - (len(a1) - v4 + 1), 0), v4 + 1):
                    for v8, v9 in v2[v5][v7].items():
                        v2[v4][v7 + 1][min(v6, v8)] = (v2[v4][v7 + 1][min(v6, v8)] + v9) % v1
        return reduce(lambda accu, x: (accu + x) % v1, (v8 * v9 % v1 for v4 in range(a2 - 1, len(v2)) for v8, v9 in v2[v4][a2].items()))
