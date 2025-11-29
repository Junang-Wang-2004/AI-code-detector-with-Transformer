import collections
from functools import reduce

class C1(object):

    def countWinningSequences(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {x: i for v3, v4 in enumerate('FWE')}
        v5 = [collections.defaultdict(int) for v6 in range(3)]
        for v3, v7 in enumerate(a1):
            v8 = [collections.defaultdict(int) for v6 in range(3)]
            v4 = v2[v7]
            for v9 in range(3):
                v10 = (v9 - v4 + 1) % 3 - 1
                if v3 == 0:
                    v8[v9][v10] = 1
                    continue
                for v11 in range(3):
                    if v11 == v9:
                        continue
                    for v12, v7 in v5[v11].items():
                        v8[v9][v12 + v10] = (v8[v9][v12 + v10] + v7) % v1
            v5 = v8
        return reduce(lambda accu, x: (accu + v4) % v1, (v7 for v9 in range(3) for v12, v7 in v5[v9].items() if v12 >= 1), 0)
