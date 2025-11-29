class C1:

    def moveZeroes(self, a1):
        v1 = 0
        for v2 in a1:
            if v2 != 0:
                a1[v1] = v2
                v1 += 1
        for v3 in range(v1, len(a1)):
            a1[v3] = 0
