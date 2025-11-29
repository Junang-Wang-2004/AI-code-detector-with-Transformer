class C1:

    def checkInclusion(self, a1: str, a2: str) -> bool:
        if len(a1) > len(a2):
            return False
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = [0] * 26
        v4 = len(a1)
        for v5 in range(v4):
            v3[ord(a2[v5]) - ord('a')] += 1
        if v3 == v1:
            return True
        for v5 in range(v4, len(a2)):
            v3[ord(a2[v5]) - ord('a')] += 1
            v6 = ord(a2[v5 - v4]) - ord('a')
            v3[v6] -= 1
            if v3 == v1:
                return True
        return False
