class C1(object):

    def closestFair(self, a1):
        v1 = str(a1)
        v2 = len(v1)
        v3 = [int(c) for v4 in v1]
        v5 = None
        if v2 % 2 == 0:
            v6 = v2 // 2
            v7 = sum((d % 2 == 0 for v8 in v3))
            if v7 == v6:
                return a1
            v9 = [0, 0]
            for v8 in v3:
                v9[v8 % 2] += 1
            for v10 in range(v2 - 1, v6 - 1, -1):
                v11 = v3[v10] % 2
                v9[v11] -= 1
                v12 = [v6 - v9[0], v6 - v9[1]]
                if min(v12) < 0:
                    continue
                v13 = v3[v10]
                v14 = v13 + 1
                v15 = v14 % 2
                if v14 <= 9 and v12[v15] >= 1:
                    v12[v15] -= 1
                    v5 = v3[:v10] + [v14] + [0] * v12[0] + [1] * v12[1]
                    break
                v14 = v13 + 2
                v15 = v14 % 2
                if v14 <= 9 and v12[v15] >= 1:
                    v12[v15] -= 1
                    v5 = v3[:v10] + [v14] + [0] * v12[0] + [1] * v12[1]
                    break
        if v5 is None:
            v16 = v2 // 2 + 1
            v5 = [1] + [0] * v16 + [1] * (v16 - 1)
        return int(''.join((str(v8) for v8 in v5)))
