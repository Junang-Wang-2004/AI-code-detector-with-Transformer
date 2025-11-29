class C1:

    def maxNiceDivisors(self, a1):
        v1 = 10 ** 9 + 7
        v2 = a1 // 3
        v3 = a1 % 3
        if v3 == 1 and v2 > 0:
            v2 -= 1
            return pow(3, v2, v1) * 4 % v1
        elif v3 == 2:
            return pow(3, v2, v1) * 2 % v1
        else:
            return pow(3, v2, v1) % v1
