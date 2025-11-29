import heapq
import itertools

class C1(object):

    def slidingPuzzle(self, a1):
        """
        """

        def dot(a1, a2):
            return a1[0] * a2[0] + a1[1] * a2[1]

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
        v5 = {(v2 * i + j + 1) % (v1 * v2): (i, j) for v6 in range(v1) for v7 in range(v2)}
        v8 = heuristic_estimate(v3, v1, v2, v5)
        v9, v10 = ([(v3.index(0), v3)], [])
        v11 = set()
        while True:
            if not v9:
                if not v10:
                    return -1
                v8 += 2
                v9, v10 = (v10, v9)
            v12, a1 = v9.pop()
            if a1 == v4:
                return v8
            if a1 not in v11:
                v11.add(a1)
                v14, v15 = divmod(v12, v2)
                for v16 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    v6, v7 = (v14 + v16[0], v15 + v16[1])
                    if 0 <= v6 < v1 and 0 <= v7 < v2:
                        v17 = v6 * v2 + v7
                        v18 = list(a1)
                        v18[v12], v18[v17] = (v18[v17], v18[v12])
                        v19 = tuple(v18)
                        v20, v21 = v5[a1[v17]]
                        v22, v23 = divmod(v12, v2)
                        v24, v25 = divmod(v17, v2)
                        v26 = dot((v22 - v24, v23 - v25), (v20 - v24, v21 - v25)) > 0
                        (v9 if v26 else v10).append((v17, v19))
        return v8
