import collections

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        a1, a2 = (tuple(a1), tuple(a2))
        v3 = collections.defaultdict(list, {a2: []})
        for v4, v5, v6, v7, v8 in a3:
            v3[v4, v5].append((v6, v7, v8))
        v9 = {a1: 0}
        v10 = set()
        while len(v10) != len(v9):
            v11, v4, v5 = min(((v9[v4, v5], v4, v5) for v4, v5 in v9.keys() if (v4, v5) not in v10))
            v10.add((v4, v5))
            if (v4, v5) == a2:
                return v11
            for v6, v7, v8 in v3[v4, v5]:
                if not ((v6, v7) not in v9 or v9[v6, v7] > v11 + v8):
                    continue
                v9[v6, v7] = v11 + v8
            for v6, v7 in v3.keys():
                if not ((v6, v7) not in v9 or v9[v6, v7] > v11 + abs(v6 - v4) + abs(v7 - v5)):
                    continue
                v9[v6, v7] = v11 + abs(v6 - v4) + abs(v7 - v5)
