from collections import deque

class C1(object):

    def latestDayToCross(self, a1, a2, a3):

        def possible(a1):
            v1 = set(((a3[k][0] - 1, a3[k][1] - 1) for v2 in range(a1)))
            v3 = [[False] * a2 for v4 in range(a1)]
            v5 = deque()
            for v6 in range(a2):
                v7 = (0, v6)
                if v7 not in v1:
                    v5.append(v7)
                    v3[0][v6] = True
            v8 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while v5:
                v9, v10 = v5.popleft()
                if v9 == a1 - 1:
                    return True
                for v11, v12 in v8:
                    v13, v14 = (v9 + v11, v10 + v12)
                    if 0 <= v13 < a1 and 0 <= v14 < a2 and (not v3[v13][v14]) and ((v13, v14) not in v1):
                        v3[v13][v14] = True
                        v5.append((v13, v14))
            return False
        v1, v2 = (0, len(a3))
        while v1 < v2:
            v3 = (v1 + v2 + 1) // 2
            if possible(v3):
                v1 = v3
            else:
                v2 = v3 - 1
        return v1
