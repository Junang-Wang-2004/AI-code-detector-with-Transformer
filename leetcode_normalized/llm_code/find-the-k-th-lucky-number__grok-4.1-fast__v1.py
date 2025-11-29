class C1:

    def kthLuckyNumber(self, a1):
        v1 = a1 + 1
        v2 = ''
        while v1 > 1:
            v2 = ('7' if v1 % 2 else '4') + v2
            v1 //= 2
        return v2
