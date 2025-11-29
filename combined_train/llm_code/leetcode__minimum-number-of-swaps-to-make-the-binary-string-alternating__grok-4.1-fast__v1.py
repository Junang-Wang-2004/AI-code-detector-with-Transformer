class C1:

    def minSwaps(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        for v4, v5 in enumerate(a1):
            if v5 == '1':
                if v4 % 2 == 0:
                    v2 += 1
                else:
                    v3 += 1
        v6 = (v1 + 1) // 2
        v7 = v1 // 2
        v8 = v2 + v3
        v9 = v2 + (v7 - v3)
        v10 = v6 - v2 + v3
        v11 = v8 == v7
        v12 = v8 == v6
        if not v11 and (not v12):
            return -1
        if v11 and v12:
            return min(v9, v10) // 2
        elif v11:
            return v9 // 2
        else:
            return v10 // 2
