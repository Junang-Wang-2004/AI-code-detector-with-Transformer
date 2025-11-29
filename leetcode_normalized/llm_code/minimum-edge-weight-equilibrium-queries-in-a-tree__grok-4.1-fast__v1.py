from collections import deque
from typing import List

class C1:

    def minOperationsQueries(self, a1: int, a2: List[List[int]], a3: List[List[int]]) -> List[int]:
        v1 = 26
        v2 = 18
        v3 = [[] for v4 in range(a1)]
        for v5, v6, v7 in a2:
            v7 -= 1
            v3[v5].append((v6, v7))
            v3[v6].append((v5, v7))
        v8 = [0] * a1
        v9 = [[-1] * v2 for v4 in range(a1)]
        v10 = [[0] * v1 for v4 in range(a1)]
        v11 = [False] * a1
        v12 = deque([0])
        v11[0] = True
        while v12:
            v5 = v12.popleft()
            for v6, v7 in v3[v5]:
                if not v11[v6]:
                    v11[v6] = True
                    v8[v6] = v8[v5] + 1
                    v9[v6][0] = v5
                    v10[v6] = v10[v5][:]
                    v10[v6][v7] += 1
                    v12.append(v6)
        for v13 in range(1, v2):
            for v5 in range(a1):
                v14 = v9[v5][v13 - 1]
                if v14 != -1:
                    v9[v5][v13] = v9[v14][v13 - 1]

        def get_lca(a1: int, a2: int) -> int:
            if v8[a1] > v8[a2]:
                a1, a2 = (a2, a1)
            v3 = v8[a2] - v8[a1]
            for v4 in range(v2):
                if v3 & 1 << v4:
                    a2 = v9[a2][v4]
            if a1 == a2:
                return a1
            for v4 in range(v2 - 1, -1, -1):
                if v9[a1][v4] != v9[a2][v4]:
                    a1 = v9[a1][v4]
                    a2 = v9[a2][v4]
            return v9[a1][0]
        v15 = [0] * len(a3)
        for v16, (v17, v18) in enumerate(a3):
            v19 = get_lca(v17, v18)
            v20 = v8[v17] + v8[v18] - 2 * v8[v19]
            v21 = max((v10[v17][v7] + v10[v18][v7] - 2 * v10[v19][v7] for v7 in range(v1)))
            v15[v16] = v20 - v21
        return v15
