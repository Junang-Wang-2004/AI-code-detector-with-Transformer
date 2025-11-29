class C1(object):

    def generateSchedule(self, a1):
        """
        """
        v1 = []
        if a1 <= 4:
            return v1
        v2 = 1
        if a1 % 2 == 0:
            for v3 in range(0, a1, 2):
                v1.append([v3, v3 + v2])
            for v3 in range(0, a1, 2):
                v1.append([v3 + v2, v3])
            for v3 in range(1, a1, 2):
                v1.append([v3, (v3 + v2) % a1])
            for v3 in range(1, a1, 2):
                v1.append([(v3 + v2) % a1, v3])
        else:
            for v3 in range(0, 2 * a1, 2):
                v1.append([v3 % a1, (v3 + v2) % a1])
            for v3 in range(0, 2 * a1, 2):
                v1.append([(v3 + v2) % a1, v3 % a1])
        for v2 in range(2, (a1 + 1) // 2):
            v4 = v1[-1][0] + 1
            for v3 in range(v4, v4 + a1):
                v1.append([v3 % a1, (v3 + v2) % a1])
            v4 = v1[-1][1] - 1
            for v3 in range(v4, v4 + a1):
                v1.append([(v3 + v2) % a1, v3 % a1])
        if a1 % 2 == 0:
            v2 = a1 // 2
            v4 = v1[-1][0] - 1
            for v3 in range(v4, v4 + a1):
                v1.append([v3 % a1, (v3 + v2) % a1])
        return v1
