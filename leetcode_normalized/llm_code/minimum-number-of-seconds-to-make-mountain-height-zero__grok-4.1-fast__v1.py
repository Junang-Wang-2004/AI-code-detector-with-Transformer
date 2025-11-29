class C1:

    def minNumberOfSeconds(self, a1, a2):
        v1 = min(a2)
        v2 = v1 * a1
        v3 = v1 * a1 * (a1 + 1) // 2

        def feasible(a1):
            v1 = 0
            for v2 in a2:
                v3, v4 = (0, a1)
                while v3 < v4:
                    v5 = (v3 + v4 + 1) // 2
                    if v2 * (v5 * (v5 + 1) // 2) <= a1:
                        v3 = v5
                    else:
                        v4 = v5 - 1
                v1 += v3
                if v1 >= a1:
                    return True
            return v1 >= a1
        while v2 < v3:
            v4 = v2 + (v3 - v2) // 2
            if feasible(v4):
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
