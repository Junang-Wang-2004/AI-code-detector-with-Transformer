class C1(object):

    def minSpeedOnTime(self, a1, a2):
        """
        """

        def ceil(a1, a2):
            return (a1 + a2 - 1) // a2

        def total_time(a1, a2):
            return sum((ceil(a1[i], a2) for v1 in range(len(a1) - 1))) + float(a1[-1]) / a2

        def check(a1, a2, a3):
            return total_time(a1, a3) <= a2
        v1 = 10 ** 7
        if not check(a1, a2, v1):
            return -1
        v2, v3 = (1, v1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(a1, a2, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v2
