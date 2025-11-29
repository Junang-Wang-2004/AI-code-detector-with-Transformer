import heapq

class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []
        events = []
        for left, right, tall in buildings:
            events.append((left, -tall, right))
            events.append((right, 0, 0))
        events.sort(key=lambda p: (p[0], p[1]))
        active = []
        outline = []
        prev_height = 0
        idx = 0
        n_events = len(events)
        while idx < n_events:
            pos = events[idx][0]
            while idx < n_events and events[idx][0] == pos and events[idx][1] < 0:
                _, neg_h, end = events[idx]
                heapq.heappush(active, (neg_h, end))
                idx += 1
            while idx < n_events and events[idx][0] == pos:
                idx += 1
            while active and active[0][1] <= pos:
                heapq.heappop(active)
            now_height = -active[0][0] if active else 0
            if now_height != prev_height:
                outline.append([pos, now_height])
                prev_height = now_height
        return outline
