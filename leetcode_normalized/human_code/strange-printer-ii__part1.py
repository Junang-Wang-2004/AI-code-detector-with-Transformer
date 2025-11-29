import collections

class C1(object):

    def isPrintable(self, a1):
        """
        """
        v1, v2 = list(range(2))

        def has_cycle(a1, a2, a3):
            v1 = [(1, a2)]
            while v1:
                v2, a2 = v1.pop()
                if v2 == 1:
                    a3[a2] = v1
                    v1.append((2, a2))
                    for v4 in a1[a2]:
                        if v4 in a3:
                            if a3[v4] == v2:
                                continue
                            return True
                        v1.append((1, v4))
                elif v2 == 2:
                    a3[a2] = v2
            return False
        v3 = collections.defaultdict(lambda: [len(a1), len(a1[0]), -1, -1])
        for v4, v5 in enumerate(a1):
            for v6, v7 in enumerate(v5):
                v3[v7][0] = min(v3[v7][0], v4)
                v3[v7][1] = min(v3[v7][1], v6)
                v3[v7][2] = max(v3[v7][2], v4)
                v3[v7][3] = max(v3[v7][3], v6)
        v8 = collections.defaultdict(set)
        for v7, (v9, v10, v11, v12) in v3.items():
            for v4 in range(v9, v11 + 1):
                for v6 in range(v10, v12 + 1):
                    if a1[v4][v6] != v7:
                        v8[v7].add(a1[v4][v6])
        v13 = {}
        return all((v7 in v13 or not has_cycle(v8, v7, v13) for v7 in v3.keys()))
