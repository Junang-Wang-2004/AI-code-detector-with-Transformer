class C1:

    def minArrayLength(self, a1, a2):
        v1 = len(a1)
        v2 = False
        for v3 in a1:
            if v3 == 0:
                v2 = True
                break
        if v2:
            return 1
        v4 = 1
        v5 = a1[0]
        v6 = 1
        while v6 < v1:
            if v5 * a1[v6] <= a2:
                v5 *= a1[v6]
            else:
                v4 += 1
                v5 = a1[v6]
            v6 += 1
        return v4
