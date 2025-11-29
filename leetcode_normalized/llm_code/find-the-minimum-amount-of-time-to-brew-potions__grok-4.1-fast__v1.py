class C1:

    def minTime(self, a1, a2):
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = a2[-1] * v1[-1]
        for v4 in range(1, len(a2)):
            v5 = a2[v4 - 1]
            v6 = a2[v4]
            v7 = 0
            for v8 in range(len(a1)):
                v9 = v1[v8 + 1]
                v10 = a1[v8]
                v11 = (v5 - v6) * v9 + v6 * v10
                if v11 > v7:
                    v7 = v11
            v3 += v7
        return v3
