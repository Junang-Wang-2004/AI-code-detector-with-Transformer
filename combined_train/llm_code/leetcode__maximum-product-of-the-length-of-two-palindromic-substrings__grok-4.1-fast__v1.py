class C1:

    def maxProduct(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0

        def get_max_end_lens(a1):
            v1 = '^#' + '#'.join(a1) + '#$'
            v2 = len(v1)
            v3 = [0] * v2
            v4 = v5 = 0
            for v6 in range(1, v2 - 1):
                v7 = 2 * v4 - v6
                if v6 < v5:
                    v3[v6] = min(v5 - v6, v3[v7])
                while v1[v6 + v3[v6] + 1] == v1[v6 - v3[v6] - 1]:
                    v3[v6] += 1
                if v6 + v3[v6] > v5:
                    v4 = v6
                    v5 = v6 + v3[v6]
            v8 = [1] * v1
            for v9 in range(v1):
                v10 = 2 * v9 + 2
                v11 = v3[v10] // 2
                v12 = v9 + v11
                v13 = 2 * v11 + 1
                v8[v12] = max(v8[v12], v13)
            for v14 in range(v1 - 2, -1, -1):
                v8[v14] = max(v8[v14], v8[v14 + 1] - 2)
            return v8
        v2 = get_max_end_lens(a1)
        v3 = get_max_end_lens(a1[::-1])
        v4 = [v3[v1 - 1 - j] for v5 in range(v1)]
        v6 = 0
        v7 = [0]
        for v5 in range(v1):
            v6 = max(v6, v2[v5])
            v7.append(v6)
        v8 = 0
        v9 = [0] * v1
        for v5 in range(v1 - 1, -1, -1):
            v8 = max(v8, v4[v5])
            v9[v5] = v8
        v10 = 0
        for v11 in range(v1):
            v10 = max(v10, v7[v11] * v9[v11])
        return v10
