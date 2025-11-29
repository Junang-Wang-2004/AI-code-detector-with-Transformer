class C1(object):

    def countGoodIntegers(self, a1, a2):
        v1 = [1]
        for v2 in range(1, a1 + 1):
            v1.append(v1[-1] * v2)
        v3 = (a1 + 1) // 2
        v4 = 10 ** (v3 - 1)
        v5 = 10 ** v3
        v6 = set()
        v7 = 0
        for v8 in range(v4, v5):
            v9 = str(v8)
            if a1 % 2:
                v10 = v9[:-1] + v9[::-1]
            else:
                v10 = v9 + v9[::-1]
            v11 = int(v10)
            if v11 % a2:
                continue
            v12 = [0] * 10
            for v13 in v10:
                v12[int(v13)] += 1
            v14 = tuple(v12)
            if v14 in v6:
                continue
            v6.add(v14)
            v15 = 1
            for v16 in v12:
                v15 *= v1[v16]
            v17 = (a1 - v12[0]) * v1[a1 - 1] // v15
            v7 += v17
        return v7
