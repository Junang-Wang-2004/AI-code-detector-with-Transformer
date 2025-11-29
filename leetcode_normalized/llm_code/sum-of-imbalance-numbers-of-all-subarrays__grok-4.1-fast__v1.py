from collections import defaultdict
from typing import List

class C1:

    def sumImbalanceNumbers(self, a1: List[int]) -> int:
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = v1 * (v1 + 1) // 2
        v3 = 0
        v4 = {}
        v5 = [-1] * v1
        for v6 in range(v1):
            v7 = a1[v6]
            v5[v6] = v4.get(v7, -1)
            v8 = v6 - v5[v6]
            v3 += v8 * (v1 - v6)
            v4[v7] = v6
        v9 = defaultdict(list)
        for v6 in range(v1):
            v9[a1[v6]].append(v6)
        v10 = 0
        v11 = set(v9.keys())

        def gaps_subs(a1: List[int], a2: int) -> int:
            if not a1:
                return v2
            v1 = 0
            v2 = -1
            for v3 in a1:
                v4 = v3 - v2 - 1
                v1 += v4 * (v4 + 1) // 2
                v2 = v3
            v4 = a2 - v2 - 1
            v1 += v4 * (v4 + 1) // 2
            return v1

        def merge_lists(a1: List[int], a2: List[int]) -> List[int]:
            v1 = []
            v2, v3 = (0, 0)
            v4, v5 = (len(a1), len(a2))
            while v2 < v4 and v3 < v5:
                if a1[v2] < a2[v3]:
                    v1.append(a1[v2])
                    v2 += 1
                else:
                    v1.append(a2[v3])
                    v3 += 1
            v1.extend(a1[v2:])
            v1.extend(a2[v3:])
            return v1
        for v12 in list(v11):
            v13 = v12 + 1
            if v13 in v11:
                v14 = v9[v12]
                v15 = v9[v13]
                v16 = gaps_subs(v14, v1)
                v17 = gaps_subs(v15, v1)
                v18 = merge_lists(v14, v15)
                v19 = gaps_subs(v18, v1)
                v20 = v2 - v16 - v17 + v19
                v10 += v20
        return v3 - v10
