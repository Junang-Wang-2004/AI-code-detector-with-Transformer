class C1(object):

    def getSum(self, a1, a2):
        """
        """
        v1 = 32
        v2, v3 = (1 << v1 >> 1, ~(~0 << v1))
        a1 = a1 | ~v3 if a1 & v2 else a1 & v3
        a2 = a2 | ~v3 if a2 & v2 else a2 & v3
        while a2:
            v6 = a1 & a2
            a1 ^= a2
            a1 = a1 | ~v3 if a1 & v2 else a1 & v3
            a2 = v6 << 1
            a2 = a2 | ~v3 if a2 & v2 else a2 & v3
        return a1

    def getSum2(self, a1, a2):
        """
        """
        v1 = 2147483647
        v2 = 2147483648
        v3 = 4294967295
        while a2:
            a1, a2 = ((a1 ^ a2) & v3, (a1 & a2) << 1 & v3)
        return a1 if a1 <= v1 else ~(a1 ^ v3)

    def minus(self, a1, a2):
        a2 = self.getSum(~a2, 1)
        return self.getSum(a1, a2)

    def multiply(self, a1, a2):
        v1 = (a1 > 0) ^ (a2 > 0)
        v2 = a1 if a1 > 0 else self.getSum(~a1, 1)
        v3 = a2 if a2 > 0 else self.getSum(~a2, 1)
        v4 = 0
        while v3 & 1:
            v4 = self.getSum(v4, v2)
            v3 >>= 1
            v2 <<= 1
        return self.getSum(~v4, 1) if v1 else v4

    def divide(self, a1, a2):
        v1 = (a1 > 0) ^ (a2 > 0)
        v2 = a1 if a1 > 0 else self.getSum(~a1, 1)
        v3 = a2 if a2 > 0 else self.getSum(~a2, 1)
        v4 = 0
        for v5 in range(31, -1, -1):
            if v2 >> v5 >= v3:
                v2 = self.minus(v2, v3 << v5)
                v4 = self.getSum(v4, 1 << v5)
        return self.getSum(~v4, 1) if v1 else v4
