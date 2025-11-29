class C1(object):

    def minDays(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4):
            v1 = v2 = 0
            for v3 in a1:
                v2 = v2 + 1 if v3 <= a4 else 0
                if v2 == a3:
                    v2 = 0
                    v1 += 1
                    if v1 == a2:
                        break
            return v1 >= a2
        if a2 * a3 > len(a1):
            return -1
        v1, v2 = (1, max(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, a2, a3, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
