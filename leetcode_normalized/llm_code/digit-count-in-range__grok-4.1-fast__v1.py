class C1:

    def digitsCount(self, a1, a2, a3):

        def count_upto(a1):
            if a1 < 0:
                return 0
            v1 = 0
            v2 = 1
            while v2 <= a1:
                v1 += a1 // (v2 * 10) * v2
                v3 = a1 % (v2 * 10)
                if v3 >= a1 * v2:
                    v1 += min(v2, v3 - a1 * v2 + 1)
                if a1 == 0:
                    v1 -= v2
                v2 *= 10
            return v1 + 1
        return count_upto(a3) - count_upto(a2 - 1)
