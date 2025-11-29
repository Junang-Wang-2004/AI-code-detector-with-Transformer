import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        fuel_heap = []
        farthest = startFuel
        station_ptr = 0
        refuels = 0
        num_stations = len(stations)
        while farthest < target:
            while station_ptr < num_stations and stations[station_ptr][0] <= farthest:
                heapq.heappush(fuel_heap, -stations[station_ptr][1])
                station_ptr += 1
            if not fuel_heap:
                return -1
            farthest += -heapq.heappop(fuel_heap)
            refuels += 1
        return refuels
