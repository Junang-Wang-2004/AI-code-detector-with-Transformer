class C1:

    def myPow(self, a1, a2):
        if a2 < 0:
            a1 = 1.0 / a1
            a2 = -a2
        v3 = 1.0
        while a2 > 0:
            if a2 % 2:
                v3 *= a1
            a1 *= a1
            a2 //= 2
        return v3
