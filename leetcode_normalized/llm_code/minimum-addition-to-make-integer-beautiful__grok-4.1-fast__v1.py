class C1(object):

    def makeIntegerBeautiful(self, a1, a2):
        v1 = 0
        v2 = a1
        while v2 > 0:
            v1 += v2 % 10
            v2 //= 10
        if v1 <= a2:
            return 0
        v3 = 0
        v4 = a1
        while v1 > a2:
            v5 = 10
            while v4 // v5 % 10 == 9:
                v5 *= 10
            v6 = v4 % v5
            v7 = 0
            v8 = v6
            while v8 > 0:
                v7 += v8 % 10
                v8 //= 10
            v1 += 1 - v7
            v9 = v5 - v6
            v3 += v9
            v4 += v9
        return v3
