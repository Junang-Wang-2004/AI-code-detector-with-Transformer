class C1:

    def minMeetingRooms(self, a1):
        v1 = []
        for v2, v3 in a1:
            v1.append((v2, 1))
            v1.append((v3, -1))
        v1.sort()
        v4, v5 = (0, 0)
        for v6, v7 in v1:
            v5 += v7
            if v5 > v4:
                v4 = v5
        return v4
