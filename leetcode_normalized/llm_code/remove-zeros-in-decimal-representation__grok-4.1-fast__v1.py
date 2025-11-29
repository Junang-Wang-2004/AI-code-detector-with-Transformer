class C1:

    def removeZeros(self, a1):
        if a1 == 0:
            return 0
        v1 = 1
        v2 = a1
        while v2 >= 10:
            v2 //= 10
            v1 *= 10
        v3 = 0
        while v1 > 0:
            v4 = a1 // v1 % 10
            if v4 != 0:
                v3 = v3 * 10 + v4
            v1 //= 10
        return v3
