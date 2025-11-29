class C1:

    def permute(self, a1, a2):
        v1 = [1] * (a1 // 2 + 2)
        for v2 in range(1, len(v1)):
            v1[v2] = v1[v2 - 1] * v2
        v3 = [False] * a1
        v4 = []
        v5 = a2
        for v6 in range(a1):
            v7 = a1 - v6 - 1
            v8 = v1[v7 // 2] * v1[(v7 + 1) // 2]
            v9 = None
            if v6 > 0:
                v10 = v4[-1]
                v9 = v10 % 2 == 0
            elif a1 % 2 == 1:
                v9 = True
            v11 = False
            for v12 in range(1, a1 + 1):
                v13 = v12 - 1
                if v3[v13]:
                    continue
                v14 = v12 % 2 == 1
                if v9 is not None and v14 != v9:
                    continue
                if v5 <= v8:
                    v3[v13] = True
                    v4.append(v12)
                    v11 = True
                    break
                v5 -= v8
            if not v11:
                return []
        return v4
