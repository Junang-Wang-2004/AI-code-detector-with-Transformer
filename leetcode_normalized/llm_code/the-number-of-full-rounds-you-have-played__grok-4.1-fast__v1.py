class C1:

    def numberOfRounds(self, a1, a2):

        def to_minutes(a1):
            return int(a1[0:2]) * 60 + int(a1[3:5])
        v1 = to_minutes(a1)
        v2 = to_minutes(a2)
        if v1 > v2:
            v2 += 1440
        v3 = v1 // 15 + (1 if v1 % 15 else 0)
        v4 = v2 // 15
        return max(v4 - v3, 0)
