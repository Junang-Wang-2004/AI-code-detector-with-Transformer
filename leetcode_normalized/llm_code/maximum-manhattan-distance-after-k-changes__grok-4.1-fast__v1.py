class C1:

    def maxDistance(self, a1: str, a2: int) -> int:
        v1 = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}
        v2, v3 = (0, 0)
        v4 = 0
        for v5 in range(1, len(a1) + 1):
            v6, v7 = v1[a1[v5 - 1]]
            v2 += v6
            v3 += v7
            v8 = abs(v2) + abs(v3)
            v4 = max(v4, min(v8 + 2 * a2, v5))
        return v4
