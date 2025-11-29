import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        availability = [(0, i) for i in range(n)]
        heapq.heapify(availability)
        counts = [0] * n
        for start, end in meetings:
            while availability and availability[0][0] < start:
                curr_time, room_id = heapq.heappop(availability)
                heapq.heappush(availability, (start, room_id))
            avail_time, room_id = heapq.heappop(availability)
            duration = end - start
            heapq.heappush(availability, (avail_time + duration, room_id))
            counts[room_id] += 1
        max_count = 0
        top_room = 0
        for i in range(n):
            if counts[i] > max_count:
                max_count = counts[i]
                top_room = i
        return top_room
