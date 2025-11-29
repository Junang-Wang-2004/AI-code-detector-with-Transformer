class C1(object):

    def possibleStringCount(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = []
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v5 = v3
            while v3 < v4 and a1[v3] == a1[v5]:
                v3 += 1
            v2.append(v3 - v5)
        v6 = len(v2)
        v7 = 1
        for v8 in v2:
            v7 = v7 * v8 % v1
        if a2 <= v6:
            return v7
        v9 = a2 - v6
        v10 = [0] * v9
        v10[0] = 1
        for v8 in v2:
            v11 = [0] * (v9 + 1)
            for v12 in range(v9):
                v11[v12 + 1] = (v11[v12] + v10[v12]) % v1
            for v12 in range(v9):
                v13 = max(0, v12 - v8 + 1)
                v10[v12] = (v11[v12 + 1] - v11[v13] + v1) % v1
        v14 = sum(v10) % v1
        return (v7 - v14 + v1) % v1
