class C1:

    def numberOfPatterns(self, a1: int, a2: int) -> int:
        v1 = 1 << 9
        v2 = [bin(i).count('1') for v3 in range(v1)]
        v4 = [[-1] * v1 for v5 in range(9)]

        def count_ways(a1: int, a2: int) -> int:
            if v4[a1][a2] >= 0:
                return v4[a1][a2]
            v1 = v2[a2]
            v2 = 1 if a1 <= v1 <= a2 else 0
            if v1 == a2:
                v4[a1][a2] = v2
                return v2
            v3, v4 = divmod(a1, 3)
            for v5 in range(9):
                if a2 & 1 << v5 == 0:
                    v6, v7 = divmod(v5, 3)
                    v8 = abs(v3 - v6)
                    v9 = abs(v4 - v7)
                    v10 = True
                    if v8 == 2 and v9 == 0 or (v8 == 0 and v9 == 2) or (v8 == 2 and v9 == 2):
                        v11 = (v3 + v6) // 2
                        v12 = (v4 + v7) // 2
                        v13 = v11 * 3 + v12
                        if a2 & 1 << v13 == 0:
                            v10 = False
                    if v10:
                        v14 = a2 | 1 << v5
                        v2 += count_ways(v5, v14)
            v4[a1][a2] = v2
            return v2
        v6 = 0
        for v7 in range(9):
            v6 += count_ways(v7, 1 << v7)
        return v6
