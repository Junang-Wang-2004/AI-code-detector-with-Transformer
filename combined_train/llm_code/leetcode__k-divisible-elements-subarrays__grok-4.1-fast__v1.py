class C1:

    def countDistinct(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + (a1[v3] % a3 == 0)
        v4 = 10 ** 9 + 7
        v5 = 131
        v6 = [0] * (v1 + 1)
        v7 = [1] * (v1 + 1)
        for v3 in range(v1):
            v6[v3 + 1] = (v6[v3] * v5 + a1[v3]) % v4
            v7[v3 + 1] = v7[v3] * v5 % v4

        def get_subarray_hash(a1, a2):
            v1 = a2 - a1 + 1
            v2 = (v6[a2 + 1] - v6[a1] * v7[v1] % v4 + v4) % v4
            return v2
        v8 = 0
        for v9 in range(1, v1 + 1):
            v10 = set()
            for v11 in range(v1 - v9 + 1):
                v12 = v11 + v9 - 1
                v13 = v2[v12 + 1] - v2[v11]
                if v13 <= a2:
                    v10.add(get_subarray_hash(v11, v12))
            v8 += len(v10)
        return v8
