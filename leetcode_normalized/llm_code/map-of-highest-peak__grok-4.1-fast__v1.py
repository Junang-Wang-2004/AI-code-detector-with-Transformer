from collections import deque

class C1:

    def highestPeak(self, a1):
        if not a1 or not a1[0]:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[-1] * v2 for v4 in range(v1)]
        v5 = deque()
        for v6 in range(v1):
            for v7 in range(v2):
                if a1[v6][v7]:
                    v3[v6][v7] = 0
                    v5.append((v6, v7))
        v8 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v5:
            v9 = len(v5)
            for v4 in range(v9):
                v10, v11 = v5.popleft()
                for v12, v13 in v8:
                    v14, v15 = (v10 + v12, v11 + v13)
                    if 0 <= v14 < v1 and 0 <= v15 < v2 and (v3[v14][v15] == -1):
                        v3[v14][v15] = v3[v10][v11] + 1
                        v5.append((v14, v15))
        return v3
