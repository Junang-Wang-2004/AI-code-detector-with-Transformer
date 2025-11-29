class C1:

    def daysBetweenDates(self, a1, a2):
        v1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def total_days_up_to(a1):
            v1 = int(a1[0:4])
            v2 = int(a1[5:7])
            v3 = int(a1[8:10])
            v4 = (v1 - 1) * 365 + (v1 - 1) // 4 - (v1 - 1) // 100 + (v1 - 1) // 400
            v5 = sum((v1[i] for v6 in range(1, v2)))
            if v2 > 2 and (v1 % 4 == 0 and (v1 % 100 != 0 or v1 % 400 == 0)):
                v5 += 1
            return v4 + v5 + v3
        return abs(total_days_up_to(a1) - total_days_up_to(a2))
