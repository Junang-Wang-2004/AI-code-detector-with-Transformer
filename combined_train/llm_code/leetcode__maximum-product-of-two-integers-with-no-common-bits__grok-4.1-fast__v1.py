class C1(object):

    def maxProduct(self, a1):
        v1 = max(a1)
        v2 = 1
        v3 = 0
        while v2 <= v1:
            v2 *= 2
            v3 += 1
        v4 = 1 << v3
        v5 = [0] * v4
        for v6 in a1:
            v5[v6] = v6
        for v7 in range(v3):
            v8 = 1 << v7
            for v9 in range(v4):
                if v9 & v8 == 0:
                    v10 = v9 | v8
                    v5[v10] = max(v5[v10], v5[v9])
        v11 = v4 - 1
        v12 = 0
        for v13 in range(v4):
            v14 = v11 ^ v13
            v15 = v5[v13] * v5[v14]
            if v15 > v12:
                v12 = v15
        return v12
