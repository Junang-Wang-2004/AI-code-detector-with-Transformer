import collections

class C1(object):

    def gridIllumination(self, a1, a2, a3):
        """
        """
        v1 = set()
        v2 = collections.defaultdict(int)
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)
        v5 = collections.defaultdict(int)
        for v6, v7 in a2:
            if (v6, v7) in v1:
                continue
            v1.add((v6, v7))
            v2[v6] += 1
            v3[v7] += 1
            v4[v6 - v7] += 1
            v5[v6 + v7] += 1
        v8 = []
        for v6, v7 in a3:
            if not (v2[v6] or v3[v7] or v4[v6 - v7] or v5[v6 + v7]):
                v8.append(0)
                continue
            v8.append(1)
            for v9 in range(max(v6 - 1, 0), min(v6 + 1, a1 - 1) + 1):
                for v10 in range(max(v7 - 1, 0), min(v7 + 1, a1 - 1) + 1):
                    if (v9, v10) not in v1:
                        continue
                    v1.remove((v9, v10))
                    v2[v9] -= 1
                    v3[v10] -= 1
                    v4[v9 - v10] -= 1
                    v5[v9 + v10] -= 1
        return v8
