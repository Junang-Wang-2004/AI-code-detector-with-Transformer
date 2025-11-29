class C1:

    def findKthNumber(self, a1, a2):

        def count(a1):
            v1 = 0
            v2 = 1
            while a1 * v2 <= a1:
                v1 += v2
                v2 *= 10
            v3 = v2 // 10
            if v3 > 0:
                v4 = a1 * v3
                v5 = min(a1, (a1 + 1) * v3 - 1)
                v6 = max(0, v5 - v4 + 1)
                v1 += v6 - v3
            return v1
        v1 = 0
        v2 = a2
        while True:
            v3 = 1 if v1 == 0 else 0
            for v4 in range(v3, 10):
                v5 = v1 * 10 + v4
                if v5 > a1:
                    continue
                v6 = count(v5)
                if v2 <= v6:
                    v1 = v5
                    if v2 == 1:
                        return v1
                    v2 -= 1
                    break
                v2 -= v6
