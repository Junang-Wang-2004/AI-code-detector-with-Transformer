class C1:

    def duplicateNumbersXOR(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = 0
        for v2, v4 in v1.items():
            if v4 == 2:
                v3 ^= v2
        return v3
