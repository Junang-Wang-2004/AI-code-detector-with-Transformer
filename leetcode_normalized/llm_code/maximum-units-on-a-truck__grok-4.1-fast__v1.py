class C1:

    def maximumUnits(self, a1, a2):
        a1.sort(key=lambda pair: -pair[1])
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while a2 > 0 and v2 < v3:
            v4, v5 = a1[v2]
            if a2 >= v4:
                v1 += v4 * v5
                a2 -= v4
            else:
                v1 += a2 * v5
                a2 = 0
            v2 += 1
        return v1
