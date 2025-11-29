class C1(object):

    def minimumLines(self, a1):

        def greatest_common_divisor(a1, a2):
            a1 = abs(a1)
            a2 = abs(a2)
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def slope_between(a1, a2):
            v1 = a2[0] - a1[0]
            v2 = a2[1] - a1[1]
            v3 = greatest_common_divisor(v1, v2)
            return (v2 // v3, v1 // v3)
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = 0
        v4 = 0
        while v4 < v2 - 1:
            v3 += 1
            v5 = slope_between(v1[v4], v1[v4 + 1])
            v6 = v4 + 1
            while v6 + 1 < v2 and slope_between(v1[v6], v1[v6 + 1]) == v5:
                v6 += 1
            v4 = v6
        return v3
