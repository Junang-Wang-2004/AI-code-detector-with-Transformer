class C1:

    def colorTheArray(self, a1, a2):
        v1 = [0] * a1
        v2 = 0
        v3 = [0] * len(a2)
        for v4 in range(len(a2)):
            v5, v6 = a2[v4]
            if v1[v5]:
                v7 = 0
                if v5 > 0 and v1[v5 - 1] == v1[v5]:
                    v7 += 1
                if v5 + 1 < a1 and v1[v5 + 1] == v1[v5]:
                    v7 += 1
                v2 -= v7
            v1[v5] = v6
            if v1[v5]:
                v8 = 0
                if v5 > 0 and v1[v5 - 1] == v1[v5]:
                    v8 += 1
                if v5 + 1 < a1 and v1[v5 + 1] == v1[v5]:
                    v8 += 1
                v2 += v8
            v3[v4] = v2
        return v3
