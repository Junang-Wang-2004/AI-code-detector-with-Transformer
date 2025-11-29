class C1:

    def countTrapezoids(self, a1):
        v1 = 10 ** 9 + 7
        v2 = {}
        for v3, v4 in a1:
            v2[v4] = v2.get(v4, 0) + 1
        v5 = list(v2.values())
        v6 = [sz * (sz - 1) // 2 % v1 for v7 in v5]
        v8 = sum(v6) % v1
        v9 = sum((pc * pc % v1 for v10 in v6)) % v1
        v11 = (v8 * v8 % v1 - v9 + v1) % v1
        v12 = pow(2, v1 - 2, v1)
        return v11 * v12 % v1
