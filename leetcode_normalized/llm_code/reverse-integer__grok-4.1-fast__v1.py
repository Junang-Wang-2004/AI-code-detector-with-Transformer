class C1:

    def reverse(self, a1):
        if not a1:
            return 0
        v1 = a1 < 0
        if v1:
            a1 = -a1
        v3 = 2147483647
        v4 = 0
        while a1:
            v5 = a1 % 10
            a1 //= 10
            if v4 > v3 // 10 or (v4 == v3 // 10 and v5 > v3 % 10):
                return 0
            v4 = v4 * 10 + v5
        return -v4 if v1 else v4
