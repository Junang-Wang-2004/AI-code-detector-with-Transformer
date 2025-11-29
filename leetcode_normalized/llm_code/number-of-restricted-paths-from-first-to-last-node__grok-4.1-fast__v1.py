import heapq

class C1:

    def countRestrictedPaths(self, a1: int, a2: list[list[int]]) -> int:
        v1 = 10 ** 9 + 7
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4 - 1].append((v5 - 1, v6))
            v2[v5 - 1].append((v4 - 1, v6))
        v7 = [float('inf')] * a1
        v7[a1 - 1] = 0
        v8 = [(0, a1 - 1)]
        while v8:
            v9, v10 = heapq.heappop(v8)
            if v9 > v7[v10]:
                continue
            for v11, v12 in v2[v10]:
                v13 = v9 + v12
                if v13 < v7[v11]:
                    v7[v11] = v13
                    heapq.heappush(v8, (v13, v11))
        v14 = sorted(range(a1), key=lambda i: v7[i])
        v15 = [0] * a1
        v15[a1 - 1] = 1
        for v10 in v14:
            for v11, v3 in v2[v10]:
                if v7[v11] > v7[v10]:
                    v15[v11] = (v15[v11] + v15[v10]) % v1
        return v15[0]
