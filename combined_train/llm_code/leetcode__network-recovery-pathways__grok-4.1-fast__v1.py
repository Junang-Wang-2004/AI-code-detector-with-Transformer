from typing import List
import sys

class C1:

    def findMaxPathScore(self, a1: List[List[int]], a2: List[bool], a3: int) -> int:
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))

        def compute_topo():
            v1 = [0] * v1
            for v2 in range(v1):
                for v3, v4 in v2[v2]:
                    v1[v3] += 1
            v5 = []
            v6 = [i for v7 in range(v1) if v1[v7] == 0]
            while v6:
                v8 = []
                for v2 in v6:
                    v5.append(v2)
                    for v3, v4 in v2[v2]:
                        v1[v3] -= 1
                        if v1[v3] == 0:
                            v8.append(v3)
                v6 = v8
            return v5
        v7 = compute_topo()
        v8 = sys.maxsize
        v9 = 0
        for v4 in range(v1):
            for v3, v6 in v2[v4]:
                v8 = min(v8, v6)
                v9 = max(v9, v6)
        v10 = float('inf')

        def feasible(a1: int) -> bool:
            v1 = [v10] * v1
            v1[0] = 0
            for v2 in v7:
                if v1[v2] == v10:
                    continue
                for v3, v4 in v2[v2]:
                    if v4 >= a1 and a2[v3]:
                        v1[v3] = min(v1[v3], v1[v2] + v4)
            return v1[v1 - 1] <= a3
        v11 = v8
        v12 = v9
        while v11 <= v12:
            v13 = v11 + (v12 - v11) // 2
            if feasible(v13):
                v11 = v13 + 1
            else:
                v12 = v13 - 1
        v14 = v12
        return v14 if v14 >= v8 else -1
