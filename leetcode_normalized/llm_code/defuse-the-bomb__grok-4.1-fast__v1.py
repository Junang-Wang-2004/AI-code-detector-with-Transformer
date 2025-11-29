class C1(object):

    def decrypt(self, a1, a2):
        v1 = len(a1)
        if a2 == 0:
            return [0] * v1
        v2 = abs(a2)
        v3 = 1 if a2 > 0 else a2
        v4 = a1 + a1
        v5 = [0] * (2 * v1 + 1)
        for v6 in range(1, 2 * v1 + 1):
            v5[v6] = v5[v6 - 1] + v4[v6 - 1]
        v7 = [0] * v1
        for v6 in range(v1):
            v8 = (v6 + v3) % v1
            if v8 + v2 <= v1:
                v7[v6] = v5[v8 + v2] - v5[v8]
            else:
                v7[v6] = v5[v1] - v5[v8] + v5[v8 + v2 - v1]
        return v7
