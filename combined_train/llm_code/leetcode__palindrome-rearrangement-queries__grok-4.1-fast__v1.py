class C1:

    def canMakePalindromeQueries(self, a1: str, a2):
        v1 = len(a1)
        v2 = v1 // 2
        v3 = ord('a')
        v4 = [0] * (v2 + 1)
        v5 = [[0] * 26 for v6 in range(v2 + 1)]
        v7 = [[0] * 26 for v6 in range(v2 + 1)]
        for v8 in range(v2):
            v9 = ord(a1[v8]) - v3
            v10 = ord(a1[v1 - 1 - v8]) - v3
            v4[v8 + 1] = v4[v8] + (1 if v9 != v10 else 0)
            v5[v8 + 1] = v5[v8][:]
            v5[v8 + 1][v9] += 1
            v7[v8 + 1] = v7[v8][:]
            v7[v8 + 1][v10] += 1

        def get_segment_freq(a1, a2, a3):
            return [a1[a3 + 1][j] - a1[a2][j] for v1 in range(26)]

        def multisets_equal(a1, a2):
            return get_segment_freq(v5, a1, a2) == get_segment_freq(v7, a1, a2)

        def is_possible(a1, a2, a3, a4):
            v1 = min(a1, a3)
            v2 = max(a2, a4)
            v3 = min(a2, a4)
            v4 = max(a1, a3)
            if v4[v1] != 0 or v4[v2] - v4[v2 + 1] != 0:
                return False
            if v3 < v4:
                if v4[v4] - v4[v3 + 1] != 0:
                    return False
                return multisets_equal(v1, v3) and multisets_equal(v4, v2)
            v5 = (a1 == v1) == (a2 == v2)
            if v5:
                return multisets_equal(v1, v2)
            v6, v7 = (v5, v7) if a1 == v1 else (v7, v5)
            v8 = get_segment_freq(v6, v1, v3)
            v9 = [v7[v4][j] - v7[v1][j] for v10 in range(26)]
            v11 = [v8[v10] - v9[v10] for v10 in range(26)]
            v12 = get_segment_freq(v7, v4, v2)
            v13 = get_segment_freq(v6, v3 + 1, v2)
            v14 = [v12[v10] - v13[v10] for v10 in range(26)]
            return v11 == v14 and all((x >= 0 for v15 in v11))
        return [is_possible(q[0], q[1], v1 - 1 - q[3], v1 - 1 - q[2]) for v11 in a2]
