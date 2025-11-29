from collections import deque

class C1(object):

    def minPushBox(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def player_can_reach(a1, a2, a3, a4, a5, a6):
            if a1 == a3 and a2 == a4:
                return True
            v1 = [(a1, a2)]
            v2 = set([(a1, a2)])
            while v1:
                v3, v4 = v1.pop()
                for v5, v6 in v3:
                    v7 = v3 + v5
                    v8 = v4 + v6
                    v9 = (v7, v8)
                    if 0 <= v7 < v1 and 0 <= v8 < v2 and (a1[v7][v8] != '#') and (v9 != (a5, a6)) and (v9 not in v2):
                        if v7 == a3 and v8 == a4:
                            return True
                        v2.add(v9)
                        v1.append(v9)
            return False
        v4 = v5 = v6 = v7 = v8 = v9 = None
        for v10 in range(v1):
            for v11 in range(v2):
                if a1[v10][v11] == 'B':
                    v4, v5 = (v10, v11)
                elif a1[v10][v11] == 'S':
                    v6, v7 = (v10, v11)
                elif a1[v10][v11] == 'T':
                    v8, v9 = (v10, v11)
        v12 = deque([(v4, v5, v6, v7, 0)])
        v13 = set([(v4, v5, v6, v7)])
        while v12:
            v14, v15, v16, v17, v18 = v12.popleft()
            if v14 == v8 and v15 == v9:
                return v18
            for v19, v20 in v3:
                v21 = v14 + v19
                v22 = v15 + v20
                if not (0 <= v21 < v1 and 0 <= v22 < v2 and (a1[v21][v22] != '#')):
                    continue
                v23 = v14 - v19
                v24 = v15 - v20
                if not (0 <= v23 < v1 and 0 <= v24 < v2 and (a1[v23][v24] != '#')):
                    continue
                if player_can_reach(v16, v17, v23, v24, v14, v15):
                    v25 = v14
                    v26 = v15
                    v27 = (v21, v22, v25, v26)
                    if v27 not in v13:
                        v13.add(v27)
                        v12.append((v21, v22, v25, v26, v18 + 1))
        return -1
