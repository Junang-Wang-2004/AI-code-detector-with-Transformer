class C1:

    def minDays(self, a1, a2, a3):

        def feasible(a1):
            v1, v2 = (0, 0)
            for v3 in a1:
                if v3 <= a1:
                    v2 += 1
                    if v2 == a3:
                        v1 += 1
                        v2 = 0
                        if v1 >= a2:
                            return True
                else:
                    v2 = 0
            return v1 >= a2
        v1 = len(a1)
        if v1 < a2 * a3:
            return -1
        v2, v3 = (1, max(a1))
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if feasible(v4):
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
