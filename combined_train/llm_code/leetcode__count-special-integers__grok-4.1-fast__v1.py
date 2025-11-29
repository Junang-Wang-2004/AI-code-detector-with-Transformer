class C1:

    def countSpecialNumbers(self, a1):
        if a1 == 0:
            return 0
        v1 = str(a1)
        v2 = [int(c) for v3 in v1]
        v4 = len(v2)
        v5 = 0
        for v6 in range(1, v4):
            v7 = 9
            for v8 in range(1, v6):
                v7 *= 10 - v8
            v5 += v7
        v9 = set()
        for v10 in range(v4):
            v11 = 1 if v10 == 0 else 0
            v12 = v2[v10]
            for v13 in range(v11, v12):
                if v13 in v9:
                    continue
                v14 = v4 - v10 - 1
                v15 = 10 - len(v9) - 1
                if v15 < v14:
                    continue
                v16 = 1
                for v17 in range(v14):
                    v16 *= v15 - v17
                v5 += v16
            v18 = v2[v10]
            if v18 in v9:
                break
            v9.add(v18)
        else:
            v5 += 1
        return v5
