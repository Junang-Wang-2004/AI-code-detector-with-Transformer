class C1:

    def largestTriangleArea(self, a1):
        v1 = 0.0
        v2 = len(a1)
        for v3 in range(v2):
            v4, v5 = a1[v3]
            for v6 in range(v3 + 1, v2):
                v7, v8 = a1[v6]
                for v9 in range(v6 + 1, v2):
                    v10, v11 = a1[v9]
                    v12 = 0.5 * abs((v7 - v4) * (v11 - v5) - (v10 - v4) * (v8 - v5))
                    if v12 > v1:
                        v1 = v12
        return v1
