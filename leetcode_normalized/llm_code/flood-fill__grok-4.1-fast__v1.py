from collections import deque

class C1:

    def floodFill(self, a1, a2, a3, a4):
        v1 = len(a1)
        if v1 == 0:
            return a1
        v2 = len(a1[0])
        v3 = a1[a2][a3]
        if v3 == a4:
            return a1
        v4 = deque([(a2, a3)])
        a1[a2][a3] = a4
        v5 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v4:
            v6, v7 = v4.popleft()
            for v8, v9 in v5:
                v10, v11 = (v6 + v8, v7 + v9)
                if 0 <= v10 < v1 and 0 <= v11 < v2 and (a1[v10][v11] == v3):
                    a1[v10][v11] = a4
                    v4.append((v10, v11))
        return a1
