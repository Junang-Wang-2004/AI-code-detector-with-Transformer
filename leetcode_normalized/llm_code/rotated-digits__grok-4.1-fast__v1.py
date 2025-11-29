class C1:

    def rotatedDigits(self, a1: int) -> int:

        def check(a1: int) -> int:
            v1 = False
            while a1 > 0:
                v2 = a1 % 10
                if v2 in (3, 4, 7):
                    return 0
                if v2 in (2, 5, 6, 9):
                    v1 = True
                a1 //= 10
            return v1
        v1 = 0
        for v2 in range(1, a1 + 1):
            v1 += check(v2)
        return v1
