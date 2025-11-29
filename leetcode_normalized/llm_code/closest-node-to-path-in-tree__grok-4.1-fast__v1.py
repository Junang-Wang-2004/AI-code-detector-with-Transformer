from collections import deque
from typing import List

class C1:

    def closestNode(self, a1: int, a2: List[List[int]], a3: List[List[int]]) -> List[int]:
        v1 = 18
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [0] * a1
        v7 = [[-1] * a1 for v3 in range(v1)]
        v8 = [False] * a1
        v9 = deque([0])
        v8[0] = True
        while v9:
            v4 = v9.popleft()
            for v5 in v2[v4]:
                if not v8[v5]:
                    v8[v5] = True
                    v6[v5] = v6[v4] + 1
                    v7[0][v5] = v4
                    v9.append(v5)
        for v10 in range(1, v1):
            for v11 in range(a1):
                if v7[v10 - 1][v11] != -1:
                    v7[v10][v11] = v7[v10 - 1][v7[v10 - 1][v11]]

        def lift(a1: int, a2: int) -> int:
            v1 = 0
            while a2 > 0:
                if a2 & 1:
                    a1 = v7[v1][a1]
                a2 >>= 1
                v1 += 1
            return a1

        def get_lca(a1: int, a2: int) -> int:
            if v6[a1] > v6[a2]:
                a1, a2 = (a2, a1)
            a2 = lift(a2, v6[a2] - v6[a1])
            if a1 == a2:
                return a1
            for v3 in range(v1 - 1, -1, -1):
                if v7[v3][a1] != v7[v3][a2]:
                    a1 = v7[v3][a1]
                    a2 = v7[v3][a2]
            return v7[0][a1]
        v12 = []
        for v13, v14, v15 in a3:
            v16 = get_lca(v13, v14)
            v17 = get_lca(v13, v15)
            v18 = get_lca(v14, v15)
            v19 = [v16, v17, v18]
            v20 = max(v19, key=lambda z: v6[z])
            v12.append(v20)
        return v12
