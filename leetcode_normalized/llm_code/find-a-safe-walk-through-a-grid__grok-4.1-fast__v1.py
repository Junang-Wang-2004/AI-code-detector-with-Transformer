from collections import deque

class C1:

    def findSafeWalk(self, a1, a2):
        if not a1 or not a1[0]:
            return False
        v1, v2 = (len(a1), len(a1[0]))
        if a1[0][0] >= a2:
            return False
        v3 = [[float('inf')] * v2 for v4 in range(v1)]
        v3[0][0] = a1[0][0]
        v5 = deque([(0, 0)])
        v6 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v7, v8 = (v1 - 1, v2 - 1)
        while v5:
            v9, v10 = v5.popleft()
            if v9 == v7 and v10 == v8:
                return True
            for v11, v12 in v6:
                v13, v14 = (v9 + v11, v10 + v12)
                if 0 <= v13 < v1 and 0 <= v14 < v2:
                    v15 = 1 if a1[v13][v14] else 0
                    v16 = v3[v9][v10] + v15
                    if v16 < a2 and v16 < v3[v13][v14]:
                        v3[v13][v14] = v16
                        if v15 == 0:
                            v5.appendleft((v13, v14))
                        else:
                            v5.append((v13, v14))
        return False
