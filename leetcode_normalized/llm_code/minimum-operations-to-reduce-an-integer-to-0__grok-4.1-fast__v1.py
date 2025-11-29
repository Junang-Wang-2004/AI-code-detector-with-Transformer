class C1:

    def minOperations(self, a1):
        v1 = 0
        while a1 > 0:
            if a1 % 2 == 0:
                a1 //= 2
            else:
                v1 += 1
                v3 = a1 // 2
                a1 = v3 + v3 % 2
        return v1
