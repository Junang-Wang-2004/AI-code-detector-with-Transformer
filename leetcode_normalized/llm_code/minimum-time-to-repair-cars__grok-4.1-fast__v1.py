class C1:

    def repairCars(self, a1, a2):
        v1 = min(a1)
        v2 = 1
        v3 = v1 * a2 * a2

        def sufficient(a1):
            v1 = 0
            for v2 in a1:
                v1 += int((a1 // v2) ** 0.5)
                if v1 >= a2:
                    return True
            return v1 >= a2
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if sufficient(v4):
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
