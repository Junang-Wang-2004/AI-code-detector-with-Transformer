class C1:

    def countKConstraintSubstrings(self, a1: str, a2: int) -> int:
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + (a1[v3] == '1')
        v4 = 0
        for v5 in range(v1):
            v6, v7 = (0, v5 + 1)
            while v6 < v7:
                v8 = (v6 + v7) // 2
                v9 = v2[v5 + 1] - v2[v8]
                v10 = v5 - v8 + 1
                v11 = v10 - v9
                if v9 <= a2 or v11 <= a2:
                    v7 = v8
                else:
                    v6 = v8 + 1
            v4 += v5 - v6 + 1
        return v4
