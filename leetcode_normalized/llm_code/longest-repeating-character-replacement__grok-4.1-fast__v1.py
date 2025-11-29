class C1:

    def characterReplacement(self, a1: str, a2: int) -> int:
        v1 = [0] * 26
        v2 = 0
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            v6 = ord(a1[v5]) - ord('A')
            v1[v6] += 1
            v4 = max(v4, v1[v6])
            while v5 - v2 + 1 > v4 + a2:
                v1[ord(a1[v2]) - ord('A')] -= 1
                v2 += 1
            v3 = max(v3, v5 - v2 + 1)
        return v3
