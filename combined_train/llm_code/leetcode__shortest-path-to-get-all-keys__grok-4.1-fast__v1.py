import collections
import heapq

class C1(object):

    def shortestPathAllKeys(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v4 = {}
        for v5 in range(v1):
            for v6 in range(v2):
                v7 = a1[v5][v6]
                if v7 != '.' and v7 != '#':
                    v4[v7] = (v5, v6)

        def get_dists(a1, a2, a3, a4, a5):
            v1 = {src: {} for v2 in a2}
            for v2 in a2:
                v3, v4 = a2[v2]
                v5 = [[False] * a4 for v6 in range(a3)]
                v5[v3][v4] = True
                v7 = collections.deque([(v3, v4, 0)])
                while v7:
                    v8, v9, v10 = v7.popleft()
                    v11 = a1[v8][v9]
                    if v11 != '.' and v11 != '#' and (v11 != v2):
                        v1[v2][v11] = v10
                        continue
                    for v12, v13 in a5:
                        v14, v15 = (v8 + v12, v9 + v13)
                        if 0 <= v14 < a3 and 0 <= v15 < a4 and (a1[v14][v15] != '#') and (not v5[v14][v15]):
                            v5[v14][v15] = True
                            v7.append((v14, v15, v10 + 1))
            return v1
        v8 = get_dists(a1, v4, v1, v2, v3)
        v9 = 0
        for v7 in v4:
            if v7.islower():
                v9 |= 1 << ord(v7) - ord('a')
        v10 = '@'
        v11 = []
        heapq.heappush(v11, (0, 0, v10))
        v12 = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        v12[v10][0] = 0
        while v11:
            v13, v14, v15 = heapq.heappop(v11)
            if v13 > v12[v15][v14]:
                continue
            if v14 == v9:
                return v13
            for v16, v17 in v8[v15].items():
                v18 = v14
                if v16.islower():
                    v19 = ord(v16) - ord('a')
                    v18 |= 1 << v19
                elif v16.isupper():
                    v20 = ord(v16) - ord('A')
                    if not v14 & 1 << v20:
                        continue
                v21 = v13 + v17
                if v21 < v12[v16][v18]:
                    v12[v16][v18] = v21
                    heapq.heappush(v11, (v21, v18, v16))
        return -1
