class C1:

    def maximum69Number(self, a1):
        v1 = 1
        while v1 * 10 <= a1:
            v1 *= 10
        while v1:
            v2 = a1 // v1 % 10
            if v2 == 6:
                return a1 + 3 * v1
            v1 //= 10
        return a1
