class C1:

    def countGoodNumbers(self, a1):
        v1 = 10 ** 9 + 7
        v2 = v1 - 1
        v3 = a1 // 2
        v4 = pow(20, v3 % v2, v1)
        if a1 % 2:
            v4 = v4 * 5 % v1
        return v4
