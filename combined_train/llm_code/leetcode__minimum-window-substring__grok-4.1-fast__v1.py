from collections import defaultdict

class C1:

    def minWindow(self, a1: str, a2: str) -> str:
        if not a1 or not a2:
            return ''
        v1 = defaultdict(int)
        for v2 in a2:
            v1[v2] += 1
        v3 = len(a2)
        v4 = defaultdict(int)
        v5 = 0
        v6 = 0
        v7 = float('inf')
        v8 = 0
        for v9 in range(len(a1)):
            v4[a1[v9]] += 1
            if a1[v9] in v1 and v4[a1[v9]] <= v1[a1[v9]]:
                v5 += 1
            while v5 == v3 and v6 <= v9:
                v10 = v9 - v6 + 1
                if v10 < v7:
                    v7 = v10
                    v8 = v6
                v4[a1[v6]] -= 1
                if a1[v6] in v1 and v4[a1[v6]] < v1[a1[v6]]:
                    v5 -= 1
                v6 += 1
        return a1[v8:v8 + v7] if v7 != float('inf') else ''
