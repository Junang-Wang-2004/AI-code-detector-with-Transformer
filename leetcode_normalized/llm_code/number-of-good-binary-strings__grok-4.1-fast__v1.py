class C1:

    def goodBinaryStrings(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7
        v2 = 0
        if a1 == 0:
            v2 = 1
        v3 = a2
        v4 = [0] * (v3 + 1)
        v5 = [0] * (v3 + 1)
        if a3 <= v3:
            v5[a3] = 1
        if a4 <= v3:
            v4[a4] = 1
        for v6 in range(1, v3 + 1):
            if v6 >= a4:
                v4[v6] = (v4[v6] + v5[v6 - a4]) % v1
            if v6 >= a3:
                v5[v6] = (v5[v6] + v4[v6 - a3]) % v1
        for v6 in range(max(a1, 1), v3 + 1):
            v2 = (v2 + v4[v6] + v5[v6]) % v1
        return v2
