class C1:

    def isFascinating(self, a1):
        v1 = [a1, a1 * 2, a1 * 3]
        v2 = [0] * 10
        for v3 in v1:
            v4 = v3
            while v4 > 0:
                v5 = v4 % 10
                v2[v5] += 1
                v4 //= 10
        if v2[0] > 0:
            return False
        for v6 in range(1, 10):
            if v2[v6] != 1:
                return False
        return True
