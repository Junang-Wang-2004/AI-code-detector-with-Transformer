class C1:

    def rangeBitwiseAnd(self, a1, a2):
        v1 = 0
        while a1 != a2:
            a1 >>= 1
            a2 >>= 1
            v1 += 1
        return a1 << v1
