from typing import List
import collections

class C1:

    def canFinish(self, a1: int, a2: List[List[int]]) -> bool:
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v3].append(v2)
        v4 = [0] * a1

        def has_cycle(a1: int) -> bool:
            if v4[a1] == 1:
                return True
            if v4[a1] == 2:
                return False
            v4[a1] = 1
            for v1 in v1[a1]:
                if has_cycle(v1):
                    return True
            v4[a1] = 2
            return False
        for v5 in range(a1):
            if has_cycle(v5):
                return False
        return True
