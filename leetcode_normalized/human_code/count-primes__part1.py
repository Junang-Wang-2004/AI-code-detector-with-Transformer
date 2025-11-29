class C1(object):

    def countPrimes(self, a1):
        if a1 <= 2:
            return 0
        v1 = [True] * (a1 // 2)
        v2 = len(v1)
        for v3 in range(3, a1, 2):
            if v3 * v3 >= a1:
                break
            if not v1[v3 // 2]:
                continue
            for v4 in range(v3 * v3, a1, 2 * v3):
                if not v1[v4 // 2]:
                    continue
                v2 -= 1
                v1[v4 // 2] = False
        return v2
