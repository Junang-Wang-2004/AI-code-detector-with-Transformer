class C1:

    def largestValsFromLabels(self, a1, a2, a3, a4):
        v1 = sorted(range(len(a1)), key=lambda x: a1[x], reverse=True)
        v2 = {}
        v3 = 0
        v4 = a3
        for v5 in v1:
            v6 = a2[v5]
            v7 = a1[v5]
            v8 = v2.get(v6, 0)
            if v8 < a4 and v4 > 0:
                v3 += v7
                v2[v6] = v8 + 1
                v4 -= 1
        return v3
