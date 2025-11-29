from collections import deque

class C1:

    def hasValidPath(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [None, [(0, 1), (0, -1)], [(-1, 0), (1, 0)], [(0, -1), (1, 0)], [(1, 0), (0, 1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]]
        if v1 == 0 or v2 == 0:
            return False
        v4 = set()
        v5 = deque([(0, 0)])
        v4.add((0, 0))
        while v5:
            v6, v7 = v5.popleft()
            if v6 == v1 - 1 and v7 == v2 - 1:
                return True
            for v8, v9 in v3[a1[v6][v7]]:
                v10 = v6 + v8
                v11 = v7 + v9
                if 0 <= v10 < v1 and 0 <= v11 < v2 and ((v10, v11) not in v4):
                    v12, v13 = (-v8, -v9)
                    if (v12, v13) in v3[a1[v10][v11]]:
                        v5.append((v10, v11))
                        v4.add((v10, v11))
        return False
