import heapq
from collections import defaultdict

class C1:

    def minOperations(self, a1, a2):
        v1 = max(a1, a2)
        v2 = 1
        while v2 < v1:
            v2 *= 10
        v2 *= 2
        v3 = list(range(v2 + 1))
        v3[0] = v3[1] = 0
        for v4 in range(2, int(v2 ** 0.5) + 1):
            if v3[v4] == v4:
                for v5 in range(v4 * v4, v2 + 1, v4):
                    if v3[v5] == v5:
                        v3[v5] = v4
        if v3[a1] == a1:
            return -1
        v6 = defaultdict(lambda: float('inf'))
        v6[a1] = a1
        v7 = [(a1, a1)]
        v8 = set()
        while v7:
            v9, v10 = heapq.heappop(v7)
            if v10 in v8:
                continue
            v8.add(v10)
            if v10 == a2:
                return v9
            v11 = 1
            while v11 <= v10:
                v12 = v10 // v11
                v13 = v12 % 10
                v14 = 1 if v12 < 10 else 0
                for v15 in (-1, 1):
                    v16 = v13 + v15
                    if v14 <= v16 <= 9:
                        v17 = v10 + v15 * v11
                        if 0 < v17 <= v2 and v3[v17] != v17:
                            v18 = v9 + v17
                            if v18 < v6[v17]:
                                v6[v17] = v18
                                heapq.heappush(v7, (v18, v17))
                v11 *= 10
        return -1
