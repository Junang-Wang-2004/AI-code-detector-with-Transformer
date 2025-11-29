class C1:

    def countSubranges(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = {}
        for v4, v5 in zip(a1, a2):
            v6 = {}
            v6[v4] = v6.get(v4, 0) + 1
            v6[-v5] = v6.get(-v5, 0) + 1
            for v7, v8 in v3.items():
                v9 = v7 + v4
                v6[v9] = (v6.get(v9, 0) + v8) % v1
                v10 = v7 - v5
                v6[v10] = (v6.get(v10, 0) + v8) % v1
            v3 = v6
            v2 = (v2 + v3.get(0, 0)) % v1
        return v2
