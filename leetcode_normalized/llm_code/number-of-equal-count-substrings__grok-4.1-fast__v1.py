class C1:

    def equalCountSubstrings(self, a1: str, a2: int) -> int:
        v1 = len(a1)
        v2 = 0
        for v3 in range(1, v1 // a2 + 1):
            v4 = v3 * a2
            v5 = [0] * 26
            v6 = 0
            for v7 in range(v1):
                v8 = ord(a1[v7]) - ord('a')
                v5[v8] += 1
                if v5[v8] == a2:
                    v6 += 1
                if v7 >= v4:
                    v9 = ord(a1[v7 - v4]) - ord('a')
                    if v5[v9] == a2:
                        v6 -= 1
                    v5[v9] -= 1
                if v7 >= v4 - 1:
                    if v6 == v3:
                        v2 += 1
        return v2
