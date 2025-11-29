class C1(object):

    def slidingPuzzle(self, a1):
        """
        """

        def heuristic_estimate(a1, a2, a3, a4):
            v1 = 0
            for v2 in range(a2):
                for v3 in range(a3):
                    v4 = a1[a3 * v2 + v3]
                    if v4 == 0:
                        continue
                    v5, v6 = a4[v4]
                    v1 += abs(v5 - v2) + abs(v6 - v3)
            return v1
        v1, v2 = (len(a1), len(a1[0]))
        v3 = tuple(itertools.chain(*a1))
        v4 = tuple(list(range(1, v1 * v2)) + [0])
        v5 = tuple(list(range(1, v1 * v2 - 2)) + [v1 * v2 - 1, v1 * v2 - 2, 0])
        v6 = {(v2 * i + j + 1) % (v1 * v2): (i, j) for v7 in range(v1) for v8 in range(v2)}
        v9 = [(0, 0, v3.index(0), v3)]
        v10 = {v3: 0}
        while v9:
            v11, v12, v13, a1 = heapq.heappop(v9)
            if a1 == v4:
                return v12
            if a1 == v5:
                return -1
            if v11 > v10[a1]:
                continue
            v15, v16 = divmod(v13, v2)
            for v17 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                v7, v8 = (v15 + v17[0], v16 + v17[1])
                if 0 <= v7 < v1 and 0 <= v8 < v2:
                    v18 = v2 * v7 + v8
                    v19 = list(a1)
                    v19[v13], v19[v18] = (v19[v18], v19[v13])
                    v20 = tuple(v19)
                    v11 = v12 + 1 + heuristic_estimate(v20, v1, v2, v6)
                    if v11 < v10.get(v20, float('inf')):
                        v10[v20] = v11
                        heapq.heappush(v9, (v11, v12 + 1, v18, v20))
        return -1
