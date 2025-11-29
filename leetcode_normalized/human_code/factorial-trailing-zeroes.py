class C1(object):

    def trailingZeroes(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += a1 / 5
            a1 /= 5
        return v1
