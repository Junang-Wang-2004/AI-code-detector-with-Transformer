from collections import defaultdict, deque

class C1:

    def checkContradictions(self, a1, a2):
        v1 = defaultdict(list)
        v2 = set()
        for (v3, v4), v5 in zip(a1, a2):
            if v5 == 0:
                continue
            v1[v3].append((v4, 1 / v5))
            v1[v4].append((v3, v5))
            v2.add(v3)
            v2.add(v4)
        v6 = {}
        v7 = 1e-09
        for v8 in list(v2):
            if v8 in v6:
                continue
            v6[v8] = 1.0
            v9 = deque([v8])
            while v9:
                v10 = v9.popleft()
                for v11, v12 in v1[v10]:
                    v13 = v6[v10] * v12
                    if v11 in v6:
                        v14 = abs(v6[v11] - v13)
                        if v14 > v7 * max(1.0, abs(v6[v11]), abs(v13)):
                            return True
                    else:
                        v6[v11] = v13
                        v9.append(v11)
        return False
