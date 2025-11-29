from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        
        stop_to_buses = defaultdict(list)
        for bus_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus_id)
        
        queue = deque([S])
        visited_stops = {S}
        visited_buses = set()
        buses_taken = 0
        
        while queue:
            level_length = len(queue)
            for _ in range(level_length):
                current = queue.popleft()
                for bus_id in stop_to_buses[current]:
                    if bus_id in visited_buses:
                        continue
                    visited_buses.add(bus_id)
                    for next_stop in routes[bus_id]:
                        if next_stop not in visited_stops:
                            if next_stop == T:
                                return buses_taken + 1
                            visited_stops.add(next_stop)
                            queue.append(next_stop)
            buses_taken += 1
        
        return -1
