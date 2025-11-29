import collections
import heapq

class C1(object):

    def shortestPathAllKeys(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs(a1, a2, a3):
            v1, v2 = a3[a2]
            v3 = [[False] * len(a1[0]) for v4 in range(len(a1))]
            v3[v1][v2] = True
            v5 = collections.deque([(v1, v2, 0)])
            v6 = {}
            while v5:
                v1, v2, v7 = v5.popleft()
                if a2 != a1[v1][v2] != '.':
                    v6[a1[v1][v2]] = v7
                    continue
                for v8 in v1:
                    v9, v10 = (v1 + v8[0], v2 + v8[1])
                    if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[v9])):
                        continue
                    if a1[v9][v10] != '#' and (not v3[v9][v10]):
                        v3[v9][v10] = True
                        v5.append((v9, v10, v7 + 1))
            return v6
        v2 = {place: (r, c) for v3, v4 in enumerate(a1) for v5, v6 in enumerate(v4) if v6 not in '.#'}
        v7 = {v6: bfs(a1, v6, v2) for v6 in v2}
        v8 = [(0, '@', 0)]
        v9 = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        v9['@'][0] = 0
        v10 = 2 ** sum((v6.islower() for v6 in v2)) - 1
        while v8:
            v11, v6, v12 = heapq.heappop(v8)
            if v9[v6][v12] < v11:
                continue
            if v12 == v10:
                return v11
            for v13, v14 in v7[v6].items():
                v15 = v12
                if v13.islower():
                    v15 |= 1 << ord(v13) - ord('a')
                elif v13.isupper():
                    if not v12 & 1 << ord(v13) - ord('A'):
                        continue
                if v11 + v14 < v9[v13][v15]:
                    v9[v13][v15] = v11 + v14
                    heapq.heappush(v8, (v11 + v14, v13, v15))
        return -1
