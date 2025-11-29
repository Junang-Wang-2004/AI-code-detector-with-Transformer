class C1:

    def isAdditiveNumber(self, a1):
        v1 = len(a1)
        for v2 in range(1, v1):
            if v2 > 1 and a1[0] == '0':
                continue
            v3 = int(a1[:v2])
            for v4 in range(v2 + 1, v1):
                v5 = a1[v2:v4]
                if len(v5) > 1 and v5[0] == '0':
                    continue
                v6 = int(v5)
                v7 = v4
                v8, v9 = (v3, v6)
                v10 = True
                while v7 < v1:
                    v11 = v8 + v9
                    v12 = str(v11)
                    v13 = len(v12)
                    if v7 + v13 > v1 or a1[v7:v7 + v13] != v12:
                        v10 = False
                        break
                    v7 += v13
                    v8, v9 = (v9, v11)
                if v10 and v7 == v1:
                    return True
        return False
