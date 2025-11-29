# Time: O(nlogn)
# Space: O(n)
from heapq import heappush, heappop


class Solution3(object):
    def minMeetingRooms(self, intervals):
        """
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        
        heappush(free_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heappop(free_rooms)
            
            heappush(free_rooms, interval[1])
        
        return len(free_rooms)
