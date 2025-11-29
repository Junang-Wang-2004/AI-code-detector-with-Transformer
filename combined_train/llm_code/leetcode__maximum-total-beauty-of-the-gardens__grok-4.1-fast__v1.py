class C1:

    def maximumBeauty(self, a1, a2, a3, a4, a5):
        a1.sort()
        v1 = 0
        while v1 < len(a1) and a1[v1] < a3:
            v1 += 1
        v2 = [0]
        for v3 in range(v1):
            v2.append(v2[-1] + a1[v3])
        v4 = 0
        v5 = v2[-1]
        v6 = 0
        v7 = len(a1)
        for v8 in range(v1 + 1):
            if v8:
                v5 -= a1[v8 - 1]
            v9 = (v1 - v8) * a3 - v5
            v10 = a2 - v9
            if v10 < 0:
                continue
            while v6 < v8 and (v6 == 0 or (v10 + v2[v6]) // v6 > a1[v6]):
                v6 += 1
            v11 = min((v10 + v2[v6]) // v6 if v6 else 0, a3 - 1)
            v12 = v11 * a5 + (v7 - v8) * a4
            if v12 > v4:
                v4 = v12
        return v4
