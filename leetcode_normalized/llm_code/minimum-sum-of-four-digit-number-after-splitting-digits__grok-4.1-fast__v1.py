class C1:

    def minimumSum(self, a1):
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2 % 10)
            v2 //= 10
        v1.sort()
        v3 = v4 = 0
        for v5, v6 in enumerate(v1):
            if v5 % 2 == 0:
                v3 = v3 * 10 + v6
            else:
                v4 = v4 * 10 + v6
        return v3 + v4
