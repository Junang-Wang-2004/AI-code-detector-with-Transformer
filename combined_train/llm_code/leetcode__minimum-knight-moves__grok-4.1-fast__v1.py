from collections import deque

class C1:

    def minKnightMoves(self, a1, a2):
        v1 = abs(a1)
        v2 = abs(a2)
        v3 = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        v4 = deque([(0, 0, 0)])
        v5 = {(0, 0)}
        while v4:
            v6, v7, v8 = v4.popleft()
            if v6 == v1 and v7 == v2:
                return v8
            for v9, v10 in v3:
                v11 = v6 + v9
                v12 = v7 + v10
                if v11 >= 0 and v12 >= 0 and ((v11, v12) not in v5):
                    if v11 == v1 and v12 == v2:
                        return v8 + 1
                    v5.add((v11, v12))
                    v4.append((v11, v12, v8 + 1))
