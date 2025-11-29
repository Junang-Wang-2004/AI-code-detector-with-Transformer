class C1(object):

    def minMeetingRooms(self, a1):
        v1, v2 = ([], [])
        for v3, v4 in a1:
            v1.append(v3)
            v2.append(v4)
        v1.sort()
        v2.sort()
        v5, v6 = (0, 0)
        v7, v8 = (0, 0)
        while v5 < len(v1):
            if v1[v5] < v2[v6]:
                v8 += 1
                v7 = max(v7, v8)
                v5 += 1
            else:
                v8 -= 1
                v6 += 1
        return v7
