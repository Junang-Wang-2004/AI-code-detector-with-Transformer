import collections

class C1(object):

    def shortestBridge(self, a1):
        v1 = len(a1)
        v2 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v3 = set()
        v4 = collections.deque()
        for v5 in range(v1):
            for v6 in range(v1):
                if a1[v5][v6] == 1:
                    v7 = collections.deque([(v5, v6)])
                    v3.add((v5, v6))
                    while v7:
                        v8, v9 = v7.popleft()
                        for v10, v11 in v2:
                            v12, v13 = (v8 + v10, v9 + v11)
                            if 0 <= v12 < v1 and 0 <= v13 < v1 and ((v12, v13) not in v3) and (a1[v12][v13] == 1):
                                v3.add((v12, v13))
                                v7.append((v12, v13))
                    v4 = collections.deque(((r, c, 0) for v14, v15 in v3))
                    break
            else:
                continue
            break
        while v4:
            v8, v9, v16 = v4.popleft()
            for v10, v11 in v2:
                v12, v13 = (v8 + v10, v9 + v11)
                if not (0 <= v12 < v1 and 0 <= v13 < v1):
                    continue
                if (v12, v13) in v3:
                    continue
                if a1[v12][v13] == 1:
                    return v16
                v3.add((v12, v13))
                v4.append((v12, v13, v16 + 1))
