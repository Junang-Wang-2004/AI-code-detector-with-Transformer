class C1:

    def getSmallestString(self, a1: str, a2: int) -> str:
        v1 = list(a1)
        v2 = len(v1)
        v3 = 0
        while v3 < v2 and a2 > 0:
            v4 = ord(v1[v3]) - ord('a')
            v5 = min(v4, 26 - v4)
            v6 = min(v5, a2)
            if v6 == v5:
                v1[v3] = 'a'
            else:
                v1[v3] = chr(ord('a') + v4 - v6)
            a2 -= v6
            v3 += 1
        return ''.join(v1)
