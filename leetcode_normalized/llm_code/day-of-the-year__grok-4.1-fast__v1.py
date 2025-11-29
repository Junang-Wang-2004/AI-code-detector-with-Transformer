class C1:

    def dayOfYear(self, a1):
        v1, v2, v3 = map(int, a1.split('-'))
        v4 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        v5 = sum(v4[:v2 - 1]) + v3
        if v2 > 2 and (v1 % 4 == 0 and (v1 % 100 != 0 or v1 % 400 == 0)):
            v5 += 1
        return v5
