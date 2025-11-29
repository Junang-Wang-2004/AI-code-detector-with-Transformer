from collections import deque

class C1:

    def shortestPathBinaryMatrix(self, a1):
        if a1[0][0] or a1[-1][-1]:
            return -1
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = set([(0, 0)])
        v4 = deque([(0, 0, 1)])
        v5 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while v4:
            v6, v7, v8 = v4.popleft()
            if v6 == v1 - 1 and v7 == v2 - 1:
                return v8
            for v9, v10 in v5:
                v11, v12 = (v6 + v9, v7 + v10)
                if 0 <= v11 < v1 and 0 <= v12 < v2 and ((v11, v12) not in v3) and (a1[v11][v12] == 0):
                    v3.add((v11, v12))
                    v4.append((v11, v12, v8 + 1))
        return -1
