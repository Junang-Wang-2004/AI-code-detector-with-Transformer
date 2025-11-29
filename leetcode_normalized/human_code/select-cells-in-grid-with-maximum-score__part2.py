class C1(object):

    def maxScore(self, a1):
        """
        """
        v1 = max((x for v2 in a1 for v3 in v2))
        v4 = [set() for v5 in range(v1)]
        for v6, v2 in enumerate(a1):
            for v3 in v2:
                v4[v3 - 1].add(v6)
        v7 = [float('-inf')] * (1 << len(a1))
        v7[0] = 0
        for v3 in range(len(v4)):
            if not v4[v3]:
                continue
            for v8 in reversed(range(len(v7))):
                for v6 in v4[v3]:
                    if v8 & 1 << v6:
                        continue
                    v7[v8 | 1 << v6] = max(v7[v8 | 1 << v6], v7[v8] + (v3 + 1))
        return max(v7)
