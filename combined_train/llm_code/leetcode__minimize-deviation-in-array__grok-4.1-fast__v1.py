class C1:

    def minimumDeviation(self, a1):
        v1 = len(a1)
        v2 = []
        for v3, v4 in enumerate(a1):
            v5 = v4 * 2 if v4 % 2 else v4
            v6 = v5
            while True:
                v2.append((v6, v3))
                if v6 % 2:
                    break
                v6 //= 2
        v2.sort()
        v7 = [0] * v1
        v8 = 0
        v9 = float('inf')
        v10 = 0
        for v3 in range(len(v2)):
            v11, v12 = v2[v3]
            v7[v12] += 1
            if v7[v12] == 1:
                v8 += 1
            while v8 == v1 and v10 <= v3:
                v13, v14 = v2[v10]
                v15, v11 = v2[v3]
                v9 = min(v9, v15 - v13)
                v7[v14] -= 1
                if v7[v14] == 0:
                    v8 -= 1
                v10 += 1
        return v9
