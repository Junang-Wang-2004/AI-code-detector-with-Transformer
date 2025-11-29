import collections
import itertools

class C1(object):

    def movesToChessboard(self, a1):
        """
        """
        v1 = len(a1)
        v2 = 0
        for v3 in (collections.Counter(list(map(tuple, a1))), collections.Counter(zip(*a1))):
            if len(v3) != 2 or sorted(v3.values()) != [v1 / 2, (v1 + 1) / 2]:
                return -1
            v4, v5 = v3
            if any((x == y for v6, v7 in zip(v4, v5))):
                return -1
            v8 = [int(v4.count(1) * 2 > v1)] if v1 % 2 else [0, 1]
            v2 += min((sum((int(i % 2 != v) for v9, v10 in enumerate(v4, begin))) for v11 in v8)) / 2
        return v2
