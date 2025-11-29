class Solution:
    def maxDistance(self, position, m):
        positions = sorted(position)
        def feasible(gap):
            placed = 1
            prev_pos = positions[0]
            for curr_pos in positions[1:]:
                if curr_pos - prev_pos >= gap:
                    placed += 1
                    prev_pos = curr_pos
            return placed >= m
        low, high = 1, positions[-1] - positions[0]
        while low < high:
            mid_val = (low + high + 1) // 2
            if feasible(mid_val):
                low = mid_val
            else:
                high = mid_val - 1
        return low
