class C1:

    def dividePlayers(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = sum(a1)
        v3 = v1 // 2
        if v2 % v3 != 0:
            return -1
        v4 = v2 // v3
        v5 = sorted(a1)
        v6 = 0
        v7 = v1 - 1
        v8 = 0
        while v6 < v7:
            if v5[v6] + v5[v7] != v4:
                return -1
            v8 += v5[v6] * v5[v7]
            v6 += 1
            v7 -= 1
        return v8
