class Solution(object):
    def maxBuilding(self, n, restrictions):
        bounds = restrictions + [[1, 0], [n, n - 1]]
        bounds.sort(key=lambda x: x[0])
        k = len(bounds)
        positions = [b[0] for b in bounds]
        init_heights = [b[1] for b in bounds]
        left_bounds = init_heights[:]
        for i in range(1, k):
            left_bounds[i] = min(left_bounds[i], left_bounds[i - 1] + positions[i] - positions[i - 1])
        right_bounds = init_heights[:]
        for i in range(k - 2, -1, -1):
            right_bounds[i] = min(right_bounds[i], right_bounds[i + 1] + positions[i + 1] - positions[i])
        result = 0
        for i in range(1, k):
            dist = positions[i] - positions[i - 1]
            ha = min(left_bounds[i - 1], right_bounds[i - 1])
            hb = min(left_bounds[i], right_bounds[i])
            peak = max(ha, hb) + (dist - abs(ha - hb)) // 2
            result = max(result, peak)
        return result
