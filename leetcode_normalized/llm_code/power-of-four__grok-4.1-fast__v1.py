class C1:

    def isPowerOfFour(self, a1):
        if a1 <= 0:
            return False
        while a1 % 4 == 0:
            a1 //= 4
        return a1 == 1
