import heapq

class Solution:
    def smallestChair(self, times, targetFriend):
        time_events = []
        for idx in range(len(times)):
            arr_time, dep_time = times[idx]
            time_events.append((arr_time, 1, idx))
            time_events.append((dep_time, 0, idx))
        time_events.sort()
        available_seats = []
        current_occupancy = {}
        seat_counter = 0
        for _, ev_type, person_id in time_events:
            if ev_type == 0:
                freed_seat = current_occupancy.pop(person_id)
                heapq.heappush(available_seats, freed_seat)
            else:
                seat_num = heapq.heappop(available_seats) if available_seats else seat_counter
                if seat_num == seat_counter:
                    seat_counter += 1
                current_occupancy[person_id] = seat_num
                if person_id == targetFriend:
                    return seat_num
