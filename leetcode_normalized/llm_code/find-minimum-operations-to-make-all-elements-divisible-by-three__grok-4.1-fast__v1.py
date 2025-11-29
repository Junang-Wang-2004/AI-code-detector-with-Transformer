class C1:

    def minimumOperations(self, a1):
        v1 = 0
        for v2 in a1:
            v3 = v2 % 3
            if v3 > 0:
                v1 += 1
        return v1
