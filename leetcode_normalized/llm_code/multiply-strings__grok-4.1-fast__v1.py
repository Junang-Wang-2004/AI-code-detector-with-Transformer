class C1:

    def multiply(self, a1, a2):
        v1 = [int(c) for v2 in reversed(a1)]
        v3 = [int(v2) for v2 in reversed(a2)]
        v4 = len(v1)
        v5 = len(v3)
        v6 = [0] * (v4 + v5)
        for v7 in range(v4):
            for v8 in range(v5):
                v6[v7 + v8] += v1[v7] * v3[v8]
        for v9 in range(v4 + v5 - 1):
            v6[v9 + 1] += v6[v9] // 10
            v6[v9] %= 10
        v10 = v4 + v5 - 1
        while v10 > 0 and v6[v10] == 0:
            v10 -= 1
        if v10 == 0 and v6[0] == 0:
            return '0'
        return ''.join((str(v6[v9]) for v9 in range(v10, -1, -1)))
