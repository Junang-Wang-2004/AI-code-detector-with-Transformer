class Solution:
    def minTaps(self, n, ranges):
        farthest_from = [0] * (n + 1)
        for tap, dist in enumerate(ranges):
            start_pos = max(0, tap - dist)
            end_pos = min(n, tap + dist)
            farthest_from[start_pos] = max(farthest_from[start_pos], end_pos)
        
        max_pos = 0
        curr_end = 0
        count = 0
        for i in range(n + 1):
            if i > max_pos:
                return -1
            max_pos = max(max_pos, farthest_from[i])
            if i == curr_end:
                count += 1
                curr_end = max_pos
                if curr_end >= n:
                    return count
        return count
