class C1:

    def maximumOddBinaryNumber(self, a1):
        v1 = 0
        for v2 in a1:
            if v2 == '1':
                v1 += 1
        v3 = len(a1) - v1
        return '1' * (v1 - 1) + '0' * v3 + '1'
