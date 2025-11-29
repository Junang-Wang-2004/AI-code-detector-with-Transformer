class C1:

    def minimumDistance(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2, v3 = a1[0]
        v4, v5 = (v2 + v3, v2 + v3)
        v6, v7 = (v2 - v3, v2 - v3)
        v8 = v9 = v10 = v11 = 0
        for v12 in range(1, v1):
            v2, v3 = a1[v12]
            v13 = v2 + v3
            v14 = v2 - v3
            if v13 < v4:
                v4 = v13
                v8 = v12
            if v13 > v5:
                v5 = v13
                v9 = v12
            if v14 < v6:
                v6 = v14
                v10 = v12
            if v14 > v7:
                v7 = v14
                v11 = v12
        v15 = v5 - v4
        v16 = v7 - v6
        if v15 >= v16:
            v17 = v9
            v18 = v8
        else:
            v17 = v11
            v18 = v10

        def get_diam(a1):
            v1 = v2 = v3 = v4 = None
            for v5 in range(v1):
                if v5 == a1:
                    continue
                v6, v7 = a1[v5]
                v8 = v6 + v7
                v9 = v6 - v7
                if v1 is None:
                    v1 = v2 = v8
                    v3 = v4 = v9
                else:
                    v1 = min(v1, v8)
                    v2 = max(v2, v8)
                    v3 = min(v3, v9)
                    v4 = max(v4, v9)
            return max(v2 - v1, v4 - v3)
        return min(get_diam(v17), get_diam(v18))
