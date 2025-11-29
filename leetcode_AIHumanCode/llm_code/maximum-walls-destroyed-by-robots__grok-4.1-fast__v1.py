import bisect

class Solution:
    def maxWalls(self, robots, distance, walls):
        events = sorted(zip(robots, distance))
        events = [(0, 0)] + events + [(float('inf'), 0)]
        ws = sorted(walls)
        no_prev_right = 0
        prev_right = 0
        for k in range(1, len(events) - 1):
            ck, dk = events[k]
            prev_ck, _ = events[k - 1]
            next_ck, _ = events[k + 1]
            right_max = min(ck + dk, next_ck - 1)
            right_add = bisect.bisect_right(ws, right_max) - bisect.bisect_left(ws, ck)
            has_right = max(no_prev_right, prev_right) + right_add
            left_base = max(ck - dk, prev_ck + 1)
            prev_max_right = min(events[k - 1][0] + events[k - 1][1], ck - 1)
            left_late = max(prev_max_right + 1, left_base)
            num_left_full = bisect.bisect_right(ws, ck) - bisect.bisect_left(ws, left_base)
            num_left_late = bisect.bisect_right(ws, ck) - bisect.bisect_left(ws, left_late)
            no_right = max(no_prev_right + num_left_full, prev_right + num_left_late)
            no_prev_right = no_right
            prev_right = has_right
        return max(no_prev_right, prev_right)
