class C1:

    def numSubseq(self, a1, a2):
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = len(a1)
        v3 = 0
        for v4 in range(v2):
            v5, v6 = (v4, v2 - 1)
            while v5 <= v6:
                v7 = (v5 + v6) // 2
                if a1[v4] + a1[v7] <= a2:
                    v5 = v7 + 1
                else:
                    v6 = v7 - 1
            v8 = v6
            if v8 >= v4:
                v3 = (v3 + pow(2, v8 - v4, v1)) % v1
        return v3
