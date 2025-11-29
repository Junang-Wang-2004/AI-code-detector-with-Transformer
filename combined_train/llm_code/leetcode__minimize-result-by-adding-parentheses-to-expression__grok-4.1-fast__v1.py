class C1:

    def minimizeResult(self, a1: str) -> str:
        v1 = a1.index('+')
        v2 = a1[:v1]
        v3 = a1[v1 + 1:]
        v4 = len(v2)
        v5 = len(v3)
        v6 = float('inf')
        v7 = 0
        v8 = 0
        for v9 in range(v4):
            v10 = v2[:v9]
            v11 = v2[v9:]
            v12 = int(v10) if v9 > 0 else 1
            v13 = int(v11)
            for v14 in range(1, v5 + 1):
                v15 = post_post[:v14]
                v16 = v3[v14:]
                v17 = int(v15)
                v18 = int(v16) if v14 < v5 else 1
                v19 = v12 * (v13 + v17) * v18
                if v19 < v6:
                    v6 = v19
                    v7 = v9
                    v8 = v1 + v14
        return a1[:v7] + '(' + a1[v7:v8 + 1] + ')' + a1[v8 + 1:]
