from collections import deque
from typing import List

class C1:

    def nearestExit(self, a1: List[List[str]], a2: List[int]) -> int:
        v1, v2 = (len(a1), len(a1[0]))
        v3, v4 = a2
        v5 = set([(v3, v4)])
        v6 = deque([(v3, v4, 0)])
        v7 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while v6:
            v8, v9, v10 = v6.popleft()
            if v10 > 0 and (v8 == 0 or v8 == v1 - 1 or v9 == 0 or (v9 == v2 - 1)):
                return v10
            for v11, v12 in v7:
                v13, v14 = (v8 + v11, v9 + v12)
                if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == '.') and ((v13, v14) not in v5):
                    v5.add((v13, v14))
                    v6.append((v13, v14, v10 + 1))
        return -1
