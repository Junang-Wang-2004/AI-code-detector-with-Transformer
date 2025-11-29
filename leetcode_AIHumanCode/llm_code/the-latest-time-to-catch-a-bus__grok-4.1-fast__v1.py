class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        waiting = 0
        idx = 0
        for t in buses[:-1]:
            while idx < len(passengers) and passengers[idx] <= t:
                waiting += 1
                idx += 1
            waiting = max(0, waiting - capacity)
        skips = max(0, waiting - capacity)
        idx -= skips
        seats_used = min(waiting, capacity)
        last_time = buses[-1]
        while idx < len(passengers) and passengers[idx] <= last_time and seats_used < capacity:
            seats_used += 1
            idx += 1
        if seats_used < capacity and (idx == 0 or passengers[idx - 1] != last_time):
            return last_time
        for k in range(idx - 1, -1, -1):
            if k == 0 or passengers[k] != passengers[k - 1] + 1:
                return passengers[k] - 1
