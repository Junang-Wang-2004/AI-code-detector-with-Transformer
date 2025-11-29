from collections import deque

class C1:

    def maxMoves(self, a1, a2, a3):
        v1 = 50
        v2 = float('inf')
        v3 = float('-inf')
        v4 = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        def compute_knight_dists(a1, a2):
            v1 = [[v2] * v1 for v2 in range(v1)]
            v1[a1][a2] = 0
            v3 = deque([(a1, a2)])
            while v3:
                v4, v5 = v3.popleft()
                v6 = v1[v4][v5]
                for v7, v8 in v4:
                    v9, v10 = (v4 + v7,)
