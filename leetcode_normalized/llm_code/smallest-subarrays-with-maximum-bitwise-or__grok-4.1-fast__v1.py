class C1:

    def smallestSubarrays(self, a1):
        v1 = len(a1)
        if not a1:
            return []
        v2 = max(a1).bit_length()
        v3 = max(v2, 1)
        v4 = [-1] * v3
        v5 = [0] * v1
        for v6 in range(v1 - 1, -1, -1):
            v7 = a1[v6]
            v8 = 0
            while v8 < v3:
                v9 = 1 << v8
                if v7 & v9:
                    v4[v8] = v6
                v8 += 1
            v10 = max(v4)
            v5[v6] = max(v10 - v6 + 1, 1)
        return v5
