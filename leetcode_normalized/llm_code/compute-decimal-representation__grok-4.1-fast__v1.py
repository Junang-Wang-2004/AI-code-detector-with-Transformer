class C1:

    def decimalRepresentation(self, a1):
        v1 = []
        if a1 == 0:
            return v1
        v2 = 1
        while v2 * 10 <= a1:
            v2 *= 10
        while a1 > 0:
            v3 = a1 // v2
            if v3:
                v1.append(v3 * v2)
            a1 %= v2
            v2 //= 10
        return v1
