import collections

class C1:

    def slidingPuzzle(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 * v2
        v4 = tuple(range(1, v3)) + (0,)
        v5 = tuple((b for v6 in a1 for v7 in v6))
        if v5 == v4:
            return 0
        v8 = {v5}
        v9 = collections.deque([(v5, 0)])
        v10 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v9:
            v11, v12 = v9.popleft()
            v13 = v11.index(0)
            v14, v15 = divmod(v13, v2)
            for v16, v17 in v10:
                v18, v19 = (v14 + v16, v15 + v17)
                if 0 <= v18 < v1 and 0 <= v19 < v2:
                    v20 = v18 * v2 + v19
                    v21 = list(v11)
                    v21[v13], v21[v20] = (v21[v20], v21[v13])
                    v22 = tuple(v21)
                    if v22 not in v8:
                        if v22 == v4:
                            return v12 + 1
                        v8.add(v22)
                        v9.append((v22, v12 + 1))
        return -1
