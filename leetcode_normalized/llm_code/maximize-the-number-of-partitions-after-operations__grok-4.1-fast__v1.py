class C1:

    def maxPartitionsAfterOperations(self, a1: str, a2: int) -> int:

        def count_bits(a1: int) -> int:
            return bin(a1).count('1')
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        v3 = [0] * (v1 + 1)
        v4 = 0
        v5 = 0
        for v6 in range(v1):
            v7 = 1 << ord(a1[v6]) - ord('a')
            v8 = v4 | v7
            if count_bits(v8) > a2:
                v5 += 1
                v4 = v7
            else:
                v4 = v8
            v2[v6 + 1] = v5
            v3[v6 + 1] = v4
        v9 = [0] * (v1 + 1)
        v10 = [0] * (v1 + 1)
        v4 = 0
        v5 = 0
        for v6 in range(v1 - 1, -1, -1):
            v7 = 1 << ord(a1[v6]) - ord('a')
            v8 = v4 | v7
            if count_bits(v8) > a2:
                v5 += 1
                v4 = v7
            else:
                v4 = v8
            v9[v6] = v5
            v10[v6] = v4
        v11 = 0
        for v12 in range(v1):
            v13 = v2[v12] + v9[v12 + 1]
            v14 = v3[v12] | v10[v12 + 1]
            v15 = count_bits(v3[v12])
            v16 = count_bits(v10[v12 + 1])
            v17 = count_bits(v14)
            v18 = 1
            if v15 == a2 == v16 and v17 != 26:
                v18 = 3
            elif v17 + (v17 != 26) > a2:
                v18 = 2
            v11 = max(v11, v13 + v18)
        return v11
