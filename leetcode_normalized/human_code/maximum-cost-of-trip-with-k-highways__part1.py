import itertools
from functools import reduce

class C1(object):

    def maximumCost(self, a1, a2, a3):
        """
        """
        if a3 + 1 > a1:
            return -1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = -1 if a3 != 1 else 0
        v7 = [[0, []] for v2 in range(1 << a1)]
        for v8 in range(a1):
            v7[1 << v8][1].append(v8)
        for v9 in range(1, a1 + 1):
            for v10 in itertools.combinations(range(a1), v9):
                v11 = reduce(lambda x, y: x | 1 << y, v10, 0)
                v12, v13 = v7[v11]
                for v14 in v13:
                    for v15, v5 in v1[v14]:
                        if v11 & 1 << v15:
                            continue
                        v16 = v11 | 1 << v15
                        if v12 + v5 < v7[v16][0]:
                            continue
                        if v12 + v5 == v7[v16][0]:
                            v7[v16][1].append(v15)
                            continue
                        v7[v16][0] = v12 + v5
                        v7[v16][1] = [v15]
                        if bin(v11).count('1') == a3:
                            v6 = max(v6, v7[v16][0])
        return v6
