class C1:

    def minEatingSpeed(self, a1, a2):
        v1 = max(a1)
        v2, v3 = (1, v1)

        def can_complete(a1, a2, a3):
            v1 = 0
            for v2 in a1:
                v1 += (v2 + a3 - 1) // a3
            return v1 <= a2
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if can_complete(a1, a2, v4):
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
