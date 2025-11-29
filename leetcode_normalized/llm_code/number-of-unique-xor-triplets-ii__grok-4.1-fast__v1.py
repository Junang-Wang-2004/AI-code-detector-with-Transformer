class C1(object):

    def uniqueXorTriplets(self, a1):
        if not a1:
            return 0
        v1 = 0
        for v2 in a1:
            if v2 > v1:
                v1 = v2
        v3 = v1.bit_length()
        v4 = 1 << v3
        v5 = [0] * v4
        for v2 in a1:
            v5[v2] += 1

        def fwht(a1, a2):
            for v1 in range(v3):
                for v2 in range(v4):
                    if v2 & 1 << v1 == 0:
                        v3 = v2 | 1 << v1
                        v4 = a1[v2]
                        v5 = a1[v3]
                        a1[v2] = v4 + v5
                        a1[v3] = v4 - v5
            if a2:
                v6 = v4
                for v2 in range(v4):
                    a1[v2] //= v6
        fwht(v5)
        for v6 in range(v4):
            v5[v6] = v5[v6] * v5[v6] * v5[v6]
        fwht(v5, True)
        return sum((1 for v7 in v5 if v7 != 0))
