class C1:

    def isHappy(self, a1: int) -> bool:

        def sum_of_squares(a1: int) -> int:
            v1 = 0
            while a1 > 0:
                v2 = a1 % 10
                v1 += v2 * v2
                a1 //= 10
            return v1
        v1 = a1
        while v1 != 1 and v1 != 4:
            v1 = sum_of_squares(v1)
        return v1 == 1
