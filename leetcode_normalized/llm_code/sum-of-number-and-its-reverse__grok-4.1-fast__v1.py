class C1:

    def sumOfNumberAndReverse(self, a1: int) -> bool:

        def get_rev(a1: int) -> int:
            v1 = 0
            v2 = 1
            v3 = a1
            while v3 > 0:
                v4 = v3 % 10
                v1 += v4 * v2
                v2 *= 10
                v3 //= 10
            return v1
        v1 = a1 // 2
        for v2 in range(v1, a1 + 1):
            if v2 + get_rev(v2) == a1:
                return True
        return False
