from collections import defaultdict

class C1:

    def maximumLength(self, a1: str) -> int:
        v1 = defaultdict(list)
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = v2
            while v2 < v3 and a1[v2] == a1[v4]:
                v2 += 1
            v1[ord(a1[v4]) - ord('a')].append(v2 - v4)
        v5 = 0
        for v6 in v1.values():
            if v6:
                v7 = sorted(v6, reverse=True)
                v8 = v7[0]
                v9 = v7[1] if len(v7) > 1 else 0
                v10 = v7[2] if len(v7) > 2 else 0
                v11 = v8 - 2
                v12 = min(v8 - 1, v9)
                v13 = v10
                v5 = max(v5, v11, v12, v13)
        return v5 if v5 > 0 else -1
