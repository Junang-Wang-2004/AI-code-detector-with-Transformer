class C1:

    def kthFactor(self, a1, a2):
        v1 = []
        v2 = 1
        while v2 * v2 <= a1:
            if a1 % v2 == 0:
                v1.append(v2)
            v2 += 1
        v3 = len(v1)
        v4 = v1 and v1[-1] * v1[-1] == a1
        v5 = v3 - int(v4)
        v6 = v3 + v5
        if a2 > v6:
            return -1
        if a2 <= v3:
            return v1[a2 - 1]
        v7 = a2 - v3
        v8 = v5 - v7
        return a1 // v1[v8]
