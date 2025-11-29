class C1(object):

    def closestDivisors(self, a1):
        v1, v2 = (a1 + 1, a1 + 2)
        v3 = int(v2 ** 0.5)
        for v4 in range(v3, 0, -1):
            if v1 % v4 == 0:
                return [v4, v1 // v4]
            if v2 % v4 == 0:
                return [v4, v2 // v4]
