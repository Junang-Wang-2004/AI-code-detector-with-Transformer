class C1:

    def maxProduct(self, a1):
        v1 = -1
        v2 = -1
        while a1 > 0:
            v3 = a1 % 10
            if v3 > v1:
                v2 = v1
                v1 = v3
            elif v3 > v2:
                v2 = v3
            a1 //= 10
        if v1 == -1:
            return 1
        if v2 == -1:
            return v1
        return v1 * v2
