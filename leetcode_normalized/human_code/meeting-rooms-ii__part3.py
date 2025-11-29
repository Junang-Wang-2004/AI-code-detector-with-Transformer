from heapq import heappush, heappop

class C1(object):

    def minMeetingRooms(self, a1):
        """
        """
        if not a1:
            return 0
        a1.sort(key=lambda x: x[0])
        v1 = []
        heappush(v1, a1[0][1])
        for v2 in a1[1:]:
            if v1[0] <= v2[0]:
                heappop(v1)
            heappush(v1, v2[1])
        return len(v1)
