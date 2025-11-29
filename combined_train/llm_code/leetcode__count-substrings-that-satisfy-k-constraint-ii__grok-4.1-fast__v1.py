class C1:

    def countKConstraintSubstrings(self, a1: str, a2: int, a3) -> list[int]:
        v1 = len(a1)
        v2 = [0] * v1
        v3 = 0
        v4 = 0
        for v5 in range(v1):
            v3 += a1[v5] == '1'
            while v3 > a2 and v5 - v4 + 1 - v3 > a2:
                v3 -= a1[v4] == '1'
                v4 += 1
            v2[v5] = v4
        v6 = [0] * (v1 + 1)
        for v5 in range(v1):
            v6[v5 + 1] = v6[v5] + (v5 - v2[v5] + 1)
        v7 = [-1] * v1
        v8 = -1
        for v9 in range(v1):
            while v8 + 1 < v1 and v2[v8 + 1] <= v9:
                v8 += 1
            v7[v9] = v8

        def triangle_size(a1):
            return a1 * (a1 + 1) // 2
        v10 = []
        for v11, v12 in a3:
            v13 = min(v7[v11], v12)
            v14 = triangle_size(v13 - v11 + 1)
            v15 = v6[v12 + 1] - v6[v13 + 1]
            v10.append(v14 + v15)
        return v10
