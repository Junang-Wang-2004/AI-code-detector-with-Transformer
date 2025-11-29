class C1:

    def maximumProduct(self, a1, a2):
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = len(a1)
        v3 = [0] * (v2 + 1)
        for v4 in range(1, v2 + 1):
            v3[v4] = v3[v4 - 1] + a1[v4 - 1]

        def check(a1):
            if a1 == 0:
                return True
            v1 = a1[a1 - 1]
            v2 = v1 * a1 - v3[a1]
            return v2 <= a2
        v5, v6 = (0, v2)
        while v5 < v6:
            v7 = (v5 + v6 + 1) // 2
            if check(v7):
                v5 = v7
            else:
                v6 = v7 - 1
        v8 = v5
        v9 = v3[v8]
        v10 = v9 + a2
        v11, v12 = divmod(v10, v8)
        v13 = pow(v11, v8 - v12, v1) * pow(v11 + 1, v12, v1) % v1
        v14 = v13
        for v15 in range(v8, v2):
            v14 = v14 * a1[v15] % v1
        return v14
