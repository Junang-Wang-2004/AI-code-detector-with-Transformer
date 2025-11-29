v1 = 4000001
v2 = [True] * (v1 + 1)
v2[0] = v2[1] = False
for v3 in range(2, int(v1 ** 0.5) + 1):
    if v2[v3]:
        for v4 in range(v3 * v3, v1 + 1, v3):
            v2[v4] = False

class C1:

    def diagonalPrime(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            for v4 in (v3, v1 - 1 - v3):
                v5 = a1[v3][v4]
                if 2 <= v5 < v1 and v2[v5]:
                    v2 = max(v2, v5)
        return v2
