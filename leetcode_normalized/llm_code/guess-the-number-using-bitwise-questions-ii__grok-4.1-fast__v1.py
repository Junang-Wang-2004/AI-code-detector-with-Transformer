class C1:

    def findNumber(self):
        v1 = 30
        v2 = [commonBits(1 << i) for v3 in range(v1)]
        v4 = [commonBits(0)] + v2[:-1]
        return sum((1 << v3 for v3, (v5, v6) in enumerate(zip(v2, v4)) if v5 - v6 == 1))
