class C1(object):

    def minMeetingRooms(self, a1):
        v1, v2 = (0, 0)
        v3 = [x for v4, v5 in a1 for v6 in [[v4, 1], [v5, -1]]]
        v3.sort()
        for v7, v8 in v3:
            v2 += v8
            v1 = max(v1, v2)
        return v1
