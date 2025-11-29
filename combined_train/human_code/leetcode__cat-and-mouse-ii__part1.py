import collections

class C1(object):

    def canMouseWin(self, a1, a2, a3):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2, v3, v4 = list(range(3))

        def parents(a1, a2, a3):
            if a3 == v4:
                for v1 in graph[a1, v3 ^ v4 ^ a3]:
                    yield (v1, a2, v3 ^ v4 ^ a3)
            else:
                for v2 in graph[a2, v3 ^ v4 ^ a3]:
                    yield (a1, v2, v3 ^ v4 ^ a3)
        v5, v6 = (len(a1), len(a1[0]))
        v7 = v5 * v6
        v8 = set()
        v9, v10, v11 = [-1] * 3
        for v12 in range(v5):
            for v13 in range(v6):
                if a1[v12][v13] == 'M':
                    v10 = v12 * v6 + v13
                elif a1[v12][v13] == 'C':
                    v11 = v12 * v6 + v13
                elif a1[v12][v13] == 'F':
                    v9 = v12 * v6 + v13
                elif a1[v12][v13] == '#':
                    v8.add(v12 * v6 + v13)
        v14 = collections.defaultdict(set)
        v15 = {v3: a3, v4: a2}
        for v12 in range(v5):
            for v13 in range(v6):
                if a1[v12][v13] == '#':
                    continue
                v16 = v12 * v6 + v13
                for v17 in [v3, v4]:
                    for v18, v19 in v1:
                        for v20 in range(v15[v17] + 1):
                            v21, v22 = (v12 + v18 * v20, v13 + v19 * v20)
                            if not (0 <= v21 < v5 and 0 <= v22 < v6 and (a1[v21][v22] != '#')):
                                break
                            v14[v16, v17].add(v21 * v6 + v22)
        v23 = {}
        for v24 in range(v7):
            for v13 in range(v7):
                v23[v24, v13, v3] = len(v14[v24, v3])
                v23[v24, v13, v4] = len(v14[v13, v4])
        v25 = collections.defaultdict(int)
        v26 = collections.deque()
        for v27 in range(v7):
            if v27 in v8 or v27 == v9:
                continue
            v25[v9, v27, v4] = v3
            v26.append((v9, v27, v4, v3))
            v25[v27, v9, v3] = v4
            v26.append((v27, v9, v3, v4))
            for v17 in [v3, v4]:
                v25[v27, v27, v17] = v4
                v26.append((v27, v27, v17, v4))
        while v26:
            v27, v28, v17, v13 = v26.popleft()
            for v29, v30, v31 in parents(v27, v28, v17):
                if v25[v29, v30, v31] != v2:
                    continue
                if v31 == v13:
                    v25[v29, v30, v31] = v13
                    v26.append((v29, v30, v31, v13))
                    continue
                v23[v29, v30, v31] -= 1
                if not v23[v29, v30, v31]:
                    v25[v29, v30, v31] = v13
                    v26.append((v29, v30, v31, v13))
        return v25[v10, v11, v3] == v3
