class Solution:
    def maxArea(self, height, positions, directions):
        n = len(positions)
        curr_sum = sum(positions)
        curr_ups = sum(1 for d in directions if d == 'U')
        events = []
        for d, p in zip(directions, positions):
            if d == 'U':
                dist = height - p
                events.append((dist, -1))
                events.append((dist + height, 1))
            else:
                dist = p
                events.append((dist, 1))
                events.append((dist + height, -1))
        events.sort()
        max_sum = curr_sum
        time = 0
        i = 0
        while i < len(events):
            t = events[i][0]
            delta_t = t - time
            v = 2 * curr_ups - n
            curr_sum += delta_t * v
            max_sum = max(max_sum, curr_sum)
            while i < len(events) and events[i][0] == t:
                curr_ups += events[i][1]
                i += 1
            time = t
        return max_sum
