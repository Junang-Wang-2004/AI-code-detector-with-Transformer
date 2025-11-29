class C1(object):

    def generateSchedule(self, a1):
        if a1 <= 4:
            return []
        v1 = []
        for v2 in range(1, a1):
            for v3 in range(a1):
                v1.append([v3, (v3 + v2) % a1])
        return v1
