from typing import List
import heapq
from collections import deque

class C1:

    def maxScore(self, a1: int, a2: List[List[int]]) -> int:
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1
        v6 = []
        for v7 in range(a1):
            if v5[v7]:
                continue
            v8 = deque([v7])
            v5[v7] = True
            v9 = [v7]
            while v8:
                v3 = v8.popleft()
                for v4 in v1[v3]:
                    if not v5[v4]:
                        v5[v4] = True
                        v8.append(v4)
                        v9.append(v4)
            v10 = len(v9)
            if v10 >= 2:
                v11 = all((len(v1[x]) == 2 for v12 in v9))
                v6.append((v10, v11))
        v6.sort(reverse=True)
        v13 = len(v6)
        v14 = {}
        for v7 in range(v13):
            v15 = a1 - 2 * v7
            if v15 >= 1:
                v14[v15] = v7
        v16 = [[v6[j][0], v6[j][1], 0, 0, 0] for v17 in range(v13)]
        v18 = []
        v19 = 0
        for v20 in range(a1, 0, -1):
            if v20 in v14:
                v21 = v14[v20]
                v22 = v16[v21]
                v22[2] = v20
                v22[3] = v20
                v22[4] = 1
                if v22[0] > 1:
                    heapq.heappush(v18, (-v20, v21))
            else:
                while v18:
                    v23, v21 = heapq.heappop(v18)
                    v24 = -v23
                    v22 = v16[v21]
                    if v22[4] >= v22[0] or v22[2] != v24:
                        continue
                    v19 += v24 * v20
                    v22[2] = v22[3]
                    v22[3] = v20
                    v22[4] += 1
                    if v22[4] == v22[0] and v22[1]:
                        v19 += v22[2] * v22[3]
                    if v22[4] < v22[0]:
                        heapq.heappush(v18, (-v22[2], v21))
                    break
        return v19
