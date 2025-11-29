from collections import deque
from typing import List
v1 = 10 ** 20

class C1:

    def minimumTotalDistance(self, a1: List[int], a2: List[List[int]]) -> int:
        a1.sort()
        a2.sort(key=lambda x: x[0])
        v1 = len(a1)
        v2 = [v1] * (v1 + 1)
        v2[0] = 0
        for v3, v4 in a2:
            v5 = [0] * (v1 + 1)
            for v6 in range(1, v1 + 1):
                v5[v6] = v5[v6 - 1] + abs(a1[v6 - 1] - v3)
            v7 = [v1] * (v1 + 1)
            v7[0] = 0
            v8 = deque()
            v8.append(0)
            for v9 in range(1, v1 + 1):
                while v8 and v8[0] < v9 - v4:
                    v8.popleft()
                if v8:
                    v10 = v2[v8[0]] - v5[v8[0]] + v5[v9]
                    v7[v9] = min(v7[v9], v10)
                v7[v9] = min(v7[v9], v2[v9])
                v11 = v2[v9] - v5[v9]
                while v8 and v2[v8[-1]] - v5[v8[-1]] >= v11:
                    v8.pop()
                v8.append(v9)
            v2 = v7
        return v2[v1]
