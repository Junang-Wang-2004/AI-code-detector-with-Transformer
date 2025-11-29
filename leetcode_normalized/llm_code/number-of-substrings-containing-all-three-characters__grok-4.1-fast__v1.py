class C1:

    def numberOfSubstrings(self, a1: str) -> int:
        v1 = v2 = v3 = -1
        v4 = 0
        v5 = len(a1)
        for v6 in range(v5):
            if a1[v6] == 'a':
                v1 = v6
            elif a1[v6] == 'b':
                v2 = v6
            else:
                v3 = v6
            v4 += min(v1, v2, v3) + 1
        return v4
