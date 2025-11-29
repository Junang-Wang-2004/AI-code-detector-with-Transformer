class C1:

    def minSpeedOnTime(self, a1, a2):

        def time_needed(a1):
            v1 = sum((d // a1 + (1 if d % a1 > 0 else 0) for v2 in a1[:-1])) + a1[-1] / a1
            return v1
        v1 = 10000000
        if time_needed(v1) > a2:
            return -1
        v2, v3 = (1, v1)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if time_needed(v4) <= a2:
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
