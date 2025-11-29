from collections import deque

class C1:

    def hasPath(self, a1, a2, a3):
        v1 = len(a1)
        if v1 == 0:
            return False
        v2 = len(a1[0])
        v3 = tuple(a2)
        v4 = tuple(a3)
        v5 = set([v3])
        v6 = deque([v3])
        v7 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v6:
            v8, v9 = v6.popleft()
            if (v8, v9) == v4:
                return True
            for v10, v11 in v7:
                v12, v13 = (v8, v9)
                while 0 <= v12 + v10 < v1 and 0 <= v13 + v11 < v2 and (a1[v12 + v10][v13 + v11] == 0):
                    v12 += v10
                    v13 += v11
                if (v12, v13) not in v5:
                    v5.add((v12, v13))
                    v6.append((v12, v13))
        return False
