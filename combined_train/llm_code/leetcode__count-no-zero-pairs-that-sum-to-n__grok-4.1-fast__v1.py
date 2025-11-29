class C1(object):

    def countNoZeroPairs(self, a1):
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2 % 10)
            v2 //= 10
        v3 = [0] * 8
        v3[0] = 1
        v4 = True
        for v5 in v1:
            v6 = [0] * 8
            v7 = 1 if v4 else 0
            v4 = False
            for v8 in range(8):
                if v3[v8] == 0:
                    continue
                v9 = v8 >> 2
                v10 = v8 >> 1 & 1
                v11 = v8 & 1
                v12 = v7 if v10 == 0 else 0
                v13 = 9 if v10 == 0 else 0
                for v14 in range(v12, v13 + 1):
                    v15 = 1 if v10 or v14 == 0 else 0
                    v16 = v7 if v11 == 0 else 0
                    v17 = 9 if v11 == 0 else 0
                    for v18 in range(v16, v17 + 1):
                        v19 = 1 if v11 or v18 == 0 else 0
                        v20 = v9 + v14 + v18
                        if v20 % 10 == v5:
                            v21 = v20 // 10
                            v22 = v21 << 2 | v15 << 1 | v19
                            v6[v22] += v3[v8]
            v3 = v6
        return sum(v3[:4])
