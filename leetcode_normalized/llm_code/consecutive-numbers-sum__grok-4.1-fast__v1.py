class C1:

    def consecutiveNumbersSum(self, a1):
        v1 = a1
        while v1 % 2 == 0:
            v1 //= 2
        v2 = 0
        v3 = 1
        while v3 * v3 <= v1:
            if v1 % v3 == 0:
                v2 += 1
                if v3 != v1 // v3:
                    v2 += 1
            v3 += 1
        return v2
