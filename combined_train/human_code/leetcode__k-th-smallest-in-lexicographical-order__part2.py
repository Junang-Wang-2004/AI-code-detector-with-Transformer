class C1(object):

    def findKthNumber(self, a1, a2):
        """
        """

        def count(a1, a2):
            v1, v2 = (0, 1)
            while a2 <= a1:
                v1 += v2
                a2 *= 10
                v2 *= 10
            v1 -= max(v2 / 10 - (a1 - a2 / 10 + 1), 0)
            return v1

        def findKthNumberHelper(a1, a2, a3, a4):
            if a3:
                a4 += 1
                if a4 == a2:
                    return (a3, a4)
            v2 = int(a3 == 0)
            while v2 <= 9:
                a3 = a3 * 10 + v2
                v4 = count(a1, a3)
                if a2 > v4 + a4:
                    a4 += v4
                elif a3 <= a1:
                    v5 = findKthNumberHelper(a1, a2, a3, a4)
                    if v5[0]:
                        return v5
                v2 += 1
                a3 /= 10
            return (0, a4)
        return findKthNumberHelper(a1, a2, 0, 0)[0]
