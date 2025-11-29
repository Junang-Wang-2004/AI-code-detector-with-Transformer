from collections import deque
from typing import List, Tuple

class C1:

    def minimumCost(self, a1: List[int], a2: List[int], a3: int) -> int:
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [0] * (v1 + 1)
        for v3 in range(v1):
            v4[v3 + 1] = v4[v3] + a2[v3]
        v5: deque[Tuple[int, int]] = deque()
        v6 = 0

        def evl(a1: Tuple[int, int], a2: int) -> int:
            return a1[0] * a2 + a1[1]

        def bd(a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]) -> bool:
            return (a2[1] - a1[1]) * (a3[0] - a2[0]) >= (a3[1] - a2[1]) * (a2[0] - a1[0])
        for v7 in range(v1 - 1, -1, -1):
            v8 = v2[v7 + 1]
            v9 = -(v6 + v2[v7 + 1] * v4[v7 + 1])
            v10 = (v8, v9)
            while len(v5) >= 2 and bd(v5[-2], v5[-1], v10):
                v5.pop()
            v5.append(v10)
            v11 = v4[v7]
            while len(v5) >= 2 and evl(v5[0], v11) >= evl(v5[1], v11):
                v5.popleft()
            v12 = evl(v5[0], v11)
            v6 = -v12 + a3 * (v4[v1] - v4[v7])
        return v6
