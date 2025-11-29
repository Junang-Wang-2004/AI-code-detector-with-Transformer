class C1(object):

    def tallestBillboard(self, a1):
        v1 = len(a1)
        v2 = v1 // 2
        v3 = a1[:v2]
        v4 = a1[v2:]

        def process(a1):
            v1 = {0: 0}
            for v2 in a1:
                v3 = v1.copy()
                for v4, v5 in v1.items():
                    v6 = v4 + v2
                    v3[v6] = max(v3.get(v6, 0), v5)
                    v7 = abs(v4 - v2)
                    v8 = v5 + min(v4, v2)
                    v3[v7] = max(v3.get(v7, 0), v8)
                v1 = v3
            return v1
        v5 = process(v3)
        v6 = process(v4)
        v7 = 0
        for v8 in v5:
            if v8 in v6:
                v7 = max(v7, v5[v8] + v6[v8] + v8)
        return v7
