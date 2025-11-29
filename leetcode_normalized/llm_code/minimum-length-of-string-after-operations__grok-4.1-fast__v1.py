class C1:

    def minimumLength(self, a1: str) -> int:
        v1 = [False] * 26
        v2 = [0] * 26
        v3 = ord('a')
        for v4 in a1:
            v5 = ord(v4) - v3
            v1[v5] = True
            v2[v5] = 1 - v2[v5]
        v6 = 0
        for v7 in range(26):
            if v1[v7]:
                v6 += 2 if v2[v7] == 0 else 1
        return v6
