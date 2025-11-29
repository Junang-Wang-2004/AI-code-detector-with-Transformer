class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0
        rows, cols = len(costs), len(costs[0])
        dp_prev = costs[0][:]
        for row in range(1, rows):
            first_min, second_min = float('inf'), float('inf')
            first_idx = -1
            for col in range(cols):
                if dp_prev[col] < first_min:
                    second_min = first_min
                    first_min = dp_prev[col]
                    first_idx = col
                elif dp_prev[col] < second_min:
                    second_min = dp_prev[col]
            dp_curr = [0] * cols
            for col in range(cols):
                add = second_min if col == first_idx else first_min
                dp_curr[col] = costs[row][col] + add
            dp_prev = dp_curr
        return min(dp_prev)
