class C1(object):

    def numDistinctIslands2(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v4 = [[False] * v2 for v5 in range(v1)]

        def find_island(a1, a2):
            from collections import deque
            v1 = deque([(a1, a2)])
            v4[a1][a2] = True
            v2 = []
            while v1:
                v3, v4 = v1.popleft()
                v2.append((v3, v4))
                for v5, v6 in v3:
                    v7, v8 = (v3 + v5, v4 + v6)
                    if 0 <= v7 < v1 and 0 <= v8 < v2 and (a1[v7][v8] == 1) and (not v4[v7][v8]):
                        v4[v7][v8] = True
                        v1.append((v7, v8))
            return v2

        def shape_key(a1):
            v1 = [lambda r, c: (r, c), lambda r, c: (r, -c), lambda r, c: (-r, c), lambda r, c: (-r, -c), lambda r, c: (c, r), lambda r, c: (c, -r), lambda r, c: (-c, r), lambda r, c: (-c, -r)]
            v2 = []
            for v3 in v1:
                v4 = sorted((v3(r, c) for v5, v6 in a1))
                v7, v8 = v4[0]
                v9 = tuple(((rr - v7, cc - v8) for v10, v11 in v4))
                v2.append(v9)
            return min(v2)
        v6 = set()
        for v7 in range(v1):
            for v8 in range(v2):
                if a1[v7][v8] == 1 and (not v4[v7][v8]):
                    v9 = find_island(v7, v8)
                    v6.add(shape_key(v9))
        return len(v6)
