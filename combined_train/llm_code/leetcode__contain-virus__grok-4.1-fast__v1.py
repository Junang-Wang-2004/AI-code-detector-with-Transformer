from collections import deque

class C1:

    def containVirus(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v4 = 0
        while True:
            v5 = set()
            v6 = []
            for v7 in range(v1):
                for v8 in range(v2):
                    if a1[v7][v8] == 1 and (v7, v8) not in v5:
                        v9 = []
                        v10 = set()
                        v11 = 0
                        v12 = deque([(v7, v8)])
                        v5.add((v7, v8))
                        while v12:
                            v13, v14 = v12.popleft()
                            v9.append((v13, v14))
                            for v15, v16 in v3:
                                v17, v18 = (v13 + v15, v14 + v16)
                                if 0 <= v17 < v1 and 0 <= v18 < v2:
                                    if a1[v17][v18] == 1 and (v17, v18) not in v5:
                                        v5.add((v17, v18))
                                        v12.append((v17, v18))
                                    elif a1[v17][v18] == 0:
                                        v10.add((v17, v18))
                                        v11 += 1
                        v6.append((len(v10), v11, v9))
            if not v6:
                break
            v6.sort(key=lambda g: -g[0])
            v19, v20, v21 = v6[0]
            v4 += v20
            for v13, v14 in v21:
                a1[v13][v14] = -1
            for v19, v19, v22 in v6[1:]:
                for v13, v14 in v22:
                    for v15, v16 in v3:
                        v17, v18 = (v13 + v15, v14 + v16)
                        if 0 <= v17 < v1 and 0 <= v18 < v2 and (a1[v17][v18] == 0):
                            a1[v17][v18] = 1
        return v4
