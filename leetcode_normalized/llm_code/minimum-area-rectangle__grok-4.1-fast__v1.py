class C1:

    def minAreaRect(self, a1):
        v1 = {(x, y) for v2, v3 in a1}
        v4 = float('inf')
        v5 = len(a1)
        for v6 in range(v5):
            v7, v8 = a1[v6]
            for v9 in range(v6 + 1, v5):
                v10, v11 = a1[v9]
                if v7 != v10 and v8 != v11:
                    if (v7, v11) in v1 and (v10, v8) in v1:
                        v12 = abs(v7 - v10) * abs(v8 - v11)
                        v4 = min(v4, v12)
        return v4 if v4 < float('inf') else 0
