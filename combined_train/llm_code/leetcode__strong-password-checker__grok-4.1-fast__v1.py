class C1:

    def strongPasswordChecker(self, a1):
        v1 = len(a1)
        v2 = any((c.islower() for v3 in a1))
        v4 = any((v3.isupper() for v3 in a1))
        v5 = any((v3.isdigit() for v3 in a1))
        v6 = 3 - int(v2) - int(v4) - int(v5)
        v7 = 0
        v8 = 0
        v9 = 0
        v10 = 0
        v11 = 0
        while v11 < v1:
            v12 = v11
            while v11 < v1 and a1[v11] == a1[v12]:
                v11 += 1
            v13 = v11 - v12
            if v13 >= 3:
                v7 += v13 // 3
                v14 = v13 % 3
                if v14 == 0:
                    v8 += 1
                elif v14 == 1:
                    v9 += 1
                else:
                    v10 += 1
        if v1 < 6:
            return max(v6, 6 - v1)
        if v1 <= 20:
            return max(v6, v7)
        v15 = v1 - 20
        v16 = 0
        v17 = v15
        v18 = min(v17, v8)
        v16 += v18
        v17 -= v18
        v19 = min(v17 // 2, v9)
        v16 += v19
        v17 -= v19 * 2
        v20 = min(v17 // 3, v10)
        v16 += v20
        return v15 + max(v6, v7 - v16)
