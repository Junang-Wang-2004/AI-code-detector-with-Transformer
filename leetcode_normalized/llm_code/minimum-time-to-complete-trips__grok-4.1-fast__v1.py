class C1:

    def minimumTime(self, a1, a2):

        def sufficient(a1):
            v1 = 0
            for v2 in a1:
                v1 += a1 // v2
                if v1 >= a2:
                    return True
            return v1 >= a2
        v1 = 1
        v2 = max(a1) * a2
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if sufficient(v3):
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
