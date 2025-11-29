class C1:

    def shipWithinDays(self, a1, a2):

        def can_ship(a1, a2, a3):
            v1 = 1
            v2 = 0
            for v3 in a1:
                if v2 + v3 > a3:
                    v1 += 1
                    v2 = v3
                else:
                    v2 += v3
            return v1 <= a2
        v1 = max(a1)
        v2 = sum(a1)
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if can_ship(a1, a2, v3):
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
