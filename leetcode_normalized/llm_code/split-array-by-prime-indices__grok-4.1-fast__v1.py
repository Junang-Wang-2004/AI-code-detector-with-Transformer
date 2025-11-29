v1 = 100010
v2 = [True] * v1
v2[0] = v2[1] = False
for v3 in range(2, int(v1 ** 0.5) + 1):
    if v2[v3]:
        for v4 in range(v3 * v3, v1, v3):
            v2[v4] = False

class C1:

    def splitArray(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        for v4 in range(v1):
            v3 += a1[v4]
            if v2[v4]:
                v2 += a1[v4]
        return abs(2 * v2 - v3)
