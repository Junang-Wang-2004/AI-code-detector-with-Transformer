from functools import lru_cache
from typing import Tuple, List
import sys

class C1:

    def earliestAndLatest(self, a1: int, a2: int, a3: int) -> List[int]:

        @lru_cache(None)
        def compute_bounds(a1: int, a2: int, a3: int) -> Tuple[int, int]:
            if a2 == a3:
                return (1, 1)
            v1, v2 = (a2, a3)
            if a2 > a3:
                a2, a3 = (a3, a2)
            v5 = sys.maxsize
            v6 = 0
            v7 = (a1 + 1) // 2
            v8 = a1 // 2
            for v9 in range(a2 + 1):
                v10 = v9 + 1
                v11 = a2 - v9
                v12 = max(v11, a3 - (v8 - v11))
                v13 = min(a3 - v10, v7 - v10 - 1)
                for v14 in range(v12, v13 + 1):
                    v15, v16 = compute_bounds(v7, v9, v14)
                    v5 = min(v5, v15 + 1)
                    v6 = max(v6, v16 + 1)
            return (v5, v6)
        v1, v2 = compute_bounds(a1, a2 - 1, a1 - a3)
        return [v1, v2]
