class C1(object):

    def sampleStats(self, a1):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = 0
        while a1[v3] == 0:
            v3 += 1
        v4 = v1 - 1
        while a1[v4] == 0:
            v4 -= 1
        v5 = 0
        for v6 in range(v1):
            v5 += v6 * a1[v6]
        v7 = v5 / v2
        v8 = -1
        v9 = 0
        for v6 in range(v1):
            if a1[v6] > v8:
                v8 = a1[v6]
                v9 = v6
        v10 = (v2 + 1) // 2
        v11 = 0
        for v6 in range(v1):
            v11 += a1[v6]
            if v11 >= v10:
                v12 = v6
                break
        v13 = (v2 + 2) // 2
        v14 = 0
        for v6 in range(v1):
            v14 += a1[v6]
            if v14 >= v13:
                v15 = v6
                break
        v16 = (v12 + v15) / 2
        return [float(v3), float(v4), v7, v16, float(v9)]
