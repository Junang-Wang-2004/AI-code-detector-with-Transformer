class C1(object):

    def countDaysTogether(self, a1, a2, a3, a4):
        """
        """
        v1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        v2 = [0] * (len(v1) + 1)
        for v3 in range(len(v1)):
            v2[v3 + 1] += v2[v3] + v1[v3]

        def day(a1):
            return v2[int(a1[:2]) - 1] + int(a1[3:])
        return max(day(min(a2, a4)) - day(max(a1, a3)) + 1, 0)
