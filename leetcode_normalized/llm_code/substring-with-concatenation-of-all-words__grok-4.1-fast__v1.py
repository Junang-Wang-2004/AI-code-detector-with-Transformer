from collections import Counter
from typing import List

class C1:

    def findSubstring(self, a1: str, a2: List[str]) -> List[int]:
        if not a2:
            return []
        v1 = len(a2[0])
        v2 = len(a2)
        v3 = v2 * v1
        if len(a1) < v3:
            return []
        v4 = Counter(a2)
        v5 = []
        for v6 in range(v1):
            v7 = Counter()
            v8 = 0
            v9 = v6
            for v10 in range(v6, len(a1) - v1 + 1, v1):
                v11 = a1[v10:v10 + v1]
                if v11 not in v4:
                    v7.clear()
                    v8 = 0
                    v9 = v10 + v1
                    continue
                v7[v11] += 1
                v8 += 1
                while v7[v11] > v4[v11]:
                    v12 = a1[v9:v9 + v1]
                    v7[v12] -= 1
                    v8 -= 1
                    v9 += v1
                if v8 == v2:
                    v5.append(v9)
        return v5
