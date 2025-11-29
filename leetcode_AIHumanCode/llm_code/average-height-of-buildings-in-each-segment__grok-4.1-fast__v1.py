class Solution:
    def averageHeightOfBuildings(self, buildings):
        events = []
        for start, end, height in buildings:
            events.append((start, 1, height))
            events.append((end, -1, height))
        events.sort()
        raw_intervals = []
        height_sum = 0
        active_count = 0
        last_position = None
        for position, change, ht in events:
            if active_count > 0 and last_position is not None and position > last_position:
                avg = height_sum // active_count
                raw_intervals.append([last_position, position, avg])
            height_sum += change * ht
            active_count += change
            last_position = position
        if not raw_intervals:
            return []
        result = [raw_intervals[0][:]]
        for interval in raw_intervals[1:]:
            prev_end, prev_avg = result[-1][1], result[-1][2]
            if prev_end == interval[0] and prev_avg == interval[2]:
                result[-1][1] = interval[1]
            else:
                result.append(interval[:])
        return result
