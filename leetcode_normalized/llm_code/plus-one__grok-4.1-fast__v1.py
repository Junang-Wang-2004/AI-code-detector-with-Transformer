class C1:

    def plusOne(self, a1):
        v1 = 0
        for v2 in a1:
            v1 = v1 * 10 + v2
        v1 += 1
        v3 = []
        while v1:
            v3.append(v1 % 10)
            v1 //= 10
        return v3[::-1]
