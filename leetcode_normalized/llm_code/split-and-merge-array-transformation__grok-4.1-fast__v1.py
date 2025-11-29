class C1:

    def minSplitMerge(self, a1, a2):
        v1 = tuple(a1)
        v2 = tuple(a2)
        if v1 == v2:
            return 0
        from collections import deque
        v3 = deque([v1])
        v4 = {v1: 0}
        while v3:
            v5 = v3.popleft()
            v6 = v4[v5]
            for v7 in self._generate_moves(v5):
                if v7 == v2:
                    return v6 + 1
                if v7 not in v4:
                    v4[v7] = v6 + 1
                    v3.append(v7)
        return -1

    def _generate_moves(self, a1):
        v1 = len(a1)
        for v2 in range(v1):
            for v3 in range(v2, v1):
                v4 = a1[v2:v3 + 1]
                v5 = a1[:v2] + a1[v3 + 1:]
                v6 = len(v5)
                for v7 in range(v6 + 1):
                    if v7 == v2:
                        continue
                    v8 = v5[:v7] + v4 + v5[v7:]
                    yield v8
