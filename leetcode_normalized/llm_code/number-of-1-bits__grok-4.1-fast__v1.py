class C1:

    def hammingWeight(self, a1: int) -> int:
        v1 = 0
        while a1:
            v1 += a1 % 2
            a1 //= 2
        return v1
