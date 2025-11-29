from functools import lru_cache
from typing import List

class C1:

    def maxHappyGroups(self, a1: int, a2: List[int]) -> int:
        v1 = [0] * a1
        for v2 in a2:
            v1[v2 % a1] += 1
        v3 = v1[0]
        v1[0] = 0
        for v4 in range(1, a1 // 2 + 1):
            v5 = a1 - v4
            v6 = v1[v4] // 2 if v4 == v5 else min(v1[v4], v1[v5])
            v3 += v6
            v1[v4] -= v6
            if v4 != v5:
                v1[v5] -= v6
        v7 = [r for v8 in range(1, a1) if v1[v8]]
        if not v7:
            return v3
        v9 = tuple((v1[v8] for v8 in v7))

        @lru_cache(maxsize=None)
        def rec(a1: int, a2: tuple) -> int:
            if not any(a2):
                return 0
            v1 = 0
            for v2, v3 in enumerate(v7):
                if a2[v2]:
                    v4 = (a1 - v3) % a1
                    v5 = list(a2)
                    v5[v2] -= 1
                    v6 = 1 if v4 == 0 else 0
                    v1 = max(v1, v6 + rec(v4, tuple(v5)))
            return v1
        return v3 + rec(0, v9)
