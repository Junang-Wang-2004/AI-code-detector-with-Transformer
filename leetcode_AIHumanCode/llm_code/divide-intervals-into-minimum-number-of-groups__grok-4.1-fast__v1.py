import heapq

class Solution:
    def minGroups(self, intervals):
        sorted_intvs = sorted(intervals, key=lambda x: x[0])
        room_ends = []
        max_needed = 0
        for start, end in sorted_intvs:
            while room_ends and room_ends[0] < start:
                heapq.heappop(room_ends)
            heapq.heappush(room_ends, end)
            max_needed = max(max_needed, len(room_ends))
        return max_needed
