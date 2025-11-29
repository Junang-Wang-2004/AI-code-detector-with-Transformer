class C1:

    def subtractProductAndSum(self, a1):
        v1, v2 = (1, 0)
        while a1 > 0:
            v3 = a1 % 10
            v1 *= v3
            v2 += v3
            a1 //= 10
        return v1 - v2
