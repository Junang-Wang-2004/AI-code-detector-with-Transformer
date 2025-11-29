class C1:

    def maxSumMinProduct(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [0] * (v2 + 1)
        for v4 in range(v2):
            v3[v4 + 1] = v3[v4] + a1[v4]
        v5 = [-1] * v2
        v6 = []
        for v4 in range(v2):
            while v6 and a1[v6[-1]] >= a1[v4]:
                v6.pop()
            if v6:
                v5[v4] = v6[-1]
            v6.append(v4)
        v7 = [v2] * v2
        v6 = []
        for v4 in range(v2):
            while v6 and a1[v6[-1]] >= a1[v4]:
                v7[v6.pop()] = v4
            v6.append(v4)
        v8 = 0
        for v4 in range(v2):
            v9 = v5[v4]
            v10 = v7[v4]
            v11 = v3[v10] - v3[v9 + 1]
            v12 = a1[v4] * v11
            if v12 > v8:
                v8 = v12
        return v8 % v1
