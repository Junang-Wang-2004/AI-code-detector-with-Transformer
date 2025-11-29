class C1:

    def takeCharacters(self, a1: str, a2: int) -> int:
        v1 = len(a1)
        v2 = [0] * 3
        v3 = v1 + 1
        v4 = 0
        for v5 in range(v1):
            v6 = ord(a1[v5]) - ord('a')
            v2[v6] += 1
            while v4 <= v5 and v2[0] >= a2 and (v2[1] >= a2) and (v2[2] >= a2):
                v3 = min(v3, v5 - v4 + 1)
                v7 = ord(a1[v4]) - ord('a')
                v2[v7] -= 1
                v4 += 1
        return v3 if v3 <= v1 else -1
