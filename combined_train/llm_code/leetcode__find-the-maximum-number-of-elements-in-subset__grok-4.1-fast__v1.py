from collections import Counter
from typing import List

class C1:

    def maximumLength(self, a1: List[int]) -> int:
        v1 = Counter(a1)
        v2 = {}

        def get_chain(a1: int) -> int:
            if a1 not in v1:
                return 0
            if a1 in v2:
                return v2[a1]
            v1 = a1 * a1
            if v1[a1] < 2 or v1 not in v1:
                v2[a1] = 1
            else:
                v2[a1] = 2 + get_chain(v1)
            return v2[a1]
        v3 = 0
        v4 = v1[1]
        if v4 > 0:
            v3 = v4 if v4 % 2 == 1 else v4 - 1
        for v5 in v1:
            if v5 != 1:
                v3 = max(v3, get_chain(v5))
        return v3
