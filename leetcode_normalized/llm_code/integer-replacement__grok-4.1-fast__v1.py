class C1:

    def integerReplacement(self, a1):
        v1 = 0
        while a1 > 1:
            if a1 % 2 == 0:
                a1 //= 2
            elif a1 == 3 or a1 % 4 == 1:
                a1 -= 1
            else:
                a1 += 1
            v1 += 1
        return v1
