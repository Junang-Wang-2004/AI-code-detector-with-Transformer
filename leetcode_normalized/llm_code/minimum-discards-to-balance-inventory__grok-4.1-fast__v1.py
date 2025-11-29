class C1:

    def minArrivalsToDiscard(self, a1, a2, a3):
        v1 = {}
        v2 = 0
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4]
            v1[v5] = v1.get(v5, 0) + 1
            if v1[v5] > a3:
                v1[v5] -= 1
                a1[v4] = -1
                v2 += 1
            v6 = v4 - a2 + 1
            if v6 >= 0:
                v7 = a1[v6]
                if v7 != -1:
                    v1[v7] -= 1
                    if v1[v7] == 0:
                        del v1[v7]
        return v2
