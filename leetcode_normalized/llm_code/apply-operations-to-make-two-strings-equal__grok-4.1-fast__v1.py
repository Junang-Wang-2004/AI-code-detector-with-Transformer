class C1:

    def minOperations(self, a1: str, a2: str, a3: int) -> int:
        v1 = -1
        v2 = 0
        v3 = 0
        v4 = 0
        for v5, v6 in enumerate(zip(a1, a2)):
            if v6[0] == v6[1]:
                continue
            v7 = float('inf') if v1 == -1 else (v5 - v1) * 2
            v8 = min(v2 + a3, v3 + v7)
            v3 = v2
            v2 = v8
            v1 = v5
            v4 ^= 1
        return v2 // 2 if v4 == 0 else -1
