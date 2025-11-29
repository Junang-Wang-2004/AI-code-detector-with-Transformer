class C1:

    def canConstruct(self, a1: str, a2: str) -> bool:
        v1 = [0] * 26
        for v2 in a2:
            v1[ord(v2) - ord('a')] += 1
        for v2 in a1:
            v3 = ord(v2) - ord('a')
            v1[v3] -= 1
            if v1[v3] < 0:
                return False
        return True
