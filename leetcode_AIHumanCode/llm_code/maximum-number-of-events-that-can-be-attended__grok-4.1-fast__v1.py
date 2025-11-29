import heapq

class Solution:
    def maxEvents(self, events):
        events.sort(key=lambda x: x[0])
        pq = []
        count = 0
        cur_day = 1
        ptr = 0
        max_end = max(x[1] for x in events)
        num_events = len(events)
        while cur_day <= max_end:
            while ptr < num_events and events[ptr][0] <= cur_day:
                heapq.heappush(pq, events[ptr][1])
                ptr += 1
            while pq and pq[0] < cur_day:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                count += 1
            cur_day += 1
        return count
