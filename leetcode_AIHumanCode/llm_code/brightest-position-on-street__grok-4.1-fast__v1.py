class Solution:
    def brightestPosition(self, lights):
        events = []
        for center, radius in lights:
            events.append((center - radius, 1))
            events.append((center + radius + 1, -1))
        events.sort()
        max_overlap = 0
        current_overlap = 0
        best_pos = None
        i = 0
        n = len(events)
        while i < n:
            time = events[i][0]
            net_delta = 0
            while i < n and events[i][0] == time:
                net_delta += events[i][1]
                i += 1
            current_overlap += net_delta
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                best_pos = time
        return best_pos
