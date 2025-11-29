class C1:

    def minBitwiseArray(self, a1):
        v1 = []
        for v2 in a1:
            if v2 % 2 == 0:
                v1.append(-1)
                continue
            v3 = 0
            v4 = v2
            while v4 % 2 == 1:
                v3 += 1
                v4 //= 2
            v5 = 1 << v3 - 1
            v1.append(v2 - v5)
        return v1
