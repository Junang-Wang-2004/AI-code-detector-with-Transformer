class C1:

    def numberOfSubstrings(self, a1: str, a2: int) -> int:
        v1 = len(a1)
        v2 = v1 * (v1 + 1) // 2
        v3 = [0] * 26
        v4 = 0
        v5 = 0
        v6 = 0
        for v7 in range(v1):
            v8 = ord(a1[v7]) - ord('a')
            if v3[v8] == a2 - 1:
                v4 += 1
            v3[v8] += 1
            while v5 <= v7 and v4 > 0:
                v9 = ord(a1[v5]) - ord('a')
                v3[v9] -= 1
                if v3[v9] == a2 - 1:
                    v4 -= 1
                v5 += 1
            v6 += v7 - v5 + 1
        return v2 - v6
