class C1(object):

    def minLargest(self, a1, a2):
        if len(a1) < len(a2):
            a1, a2 = (a2, a1)
        v3 = [x % 2 for v4 in a1]
        v5 = [v4 % 2 for v4 in a2]
        v6, v7 = (len(v3), len(v5))
        v8 = [float('inf')] * (v7 + 1)
        v8[0] = 0
        for v9 in range(1, v7 + 1):
            v10 = v8[v9 - 1]
            v11 = 2 if v10 % 2 == v5[v9 - 1] else 1
            v8[v9] = v10 + v11
        for v12 in range(1, v6 + 1):
            v13 = [float('inf')] * (v7 + 1)
            for v9 in range(v7 + 1):
                v14 = v8[v9]
                v15 = 2 if v14 % 2 == v3[v12 - 1] else 1
                v13[v9] = v14 + v15
                if v9 > 0:
                    v16 = v13[v9 - 1]
                    v17 = 2 if v16 % 2 == v5[v9 - 1] else 1
                    v13[v9] = min(v13[v9], v16 + v17)
            v8 = v13
        return v8[v7]
