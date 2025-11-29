from collections import deque

class C1:

    def maximumMinimumPath(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = sorted(set((a1[i][j] for v4 in range(v1) for v5 in range(v2))))

        def can_reach(a1):
            if a1[0][0] < a1 or a1[v1 - 1][v2 - 1] < a1:
                return False
            v1 = [[False] * v2 for v2 in range(v1)]
            v3 = deque([(0, 0)])
            v1[0][0] = True
            v4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while v3:
                v5, v6 = v3.popleft()
                if v5 == v1 - 1 and v6 == v2 - 1:
                    return True
                for v7, v8 in v4:
                    v9 = v5 + v7
                    v10 = v6 + v8
                    if 0 <= v9 < v1 and 0 <= v10 < v2 and (not v1[v9][v10]) and (a1[v9][v10] >= a1):
                        v1[v9][v10] = True
                        v3.append((v9, v10))
            return False
        v6, v7 = (0, len(v3) - 1)
        while v6 <= v7:
            v8 = (v6 + v7) // 2
            if can_reach(v3[v8]):
                v6 = v8 + 1
            else:
                v7 = v8 - 1
        return v3[v7]
