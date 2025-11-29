class C1:

    def maxProduct(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = 0
            for v4 in set(v2):
                v3 |= 1 << ord(v4) - 97
            v1[v3] = max(v1.get(v3, 0), len(v2))
        v5 = sorted([(ln, mk) for v6, v7 in v1.items()], reverse=True)
        v8 = 0
        v9 = len(v5)
        for v10 in range(v9):
            v11, v12 = v5[v10]
            if v11 * v11 <= v8:
                break
            for v13 in range(v10 + 1, v9):
                v14, v15 = v5[v13]
                if v11 * v14 <= v8:
                    break
                if v12 & v15 == 0:
                    v8 = max(v8, v11 * v14)
        return v8
