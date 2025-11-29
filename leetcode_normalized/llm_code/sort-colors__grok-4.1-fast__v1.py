class C1:

    def sortColors(self, a1):
        v1 = v2 = v3 = 0
        for v4 in a1:
            if v4 == 0:
                v1 += 1
            elif v4 == 1:
                v2 += 1
            else:
                v3 += 1
        for v5 in range(len(a1)):
            if v5 < v1:
                a1[v5] = 0
            elif v5 < v1 + v2:
                a1[v5] = 1
            else:
                a1[v5] = 2
