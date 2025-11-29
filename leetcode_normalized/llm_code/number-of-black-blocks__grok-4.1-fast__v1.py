from collections import defaultdict
from typing import List

class C1:

    def countBlackBlocks(self, a1: int, a2: int, a3: List[List[int]]) -> List[int]:
        v1 = defaultdict(int)
        for v2, v3 in a3:
            for v4 in range(-1, 1):
                v5 = v2 + v4
                if 0 <= v5 < a1 - 1:
                    for v6 in range(-1, 1):
                        v7 = v3 + v6
                        if 0 <= v7 < a2 - 1:
                            v1[v5, v7] += 1
        v8 = [0] * 5
        for v9 in v1.values():
            v8[v9] += 1
        v10 = (a1 - 1) * (a2 - 1)
        v8[0] = v10 - sum(v8[1:])
        return v8
