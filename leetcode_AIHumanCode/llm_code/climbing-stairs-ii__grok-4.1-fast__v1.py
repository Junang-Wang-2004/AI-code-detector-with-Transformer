class Solution:
    def climbStairs(self, n, costs):
        if n == 0:
            return 0
        window = [float('inf'), float('inf'), 0]
        jumps = [9, 4, 1]
        for i in range(n):
            current = costs[i] + min(window[k] + jumps[k] for k in range(3))
            window = window[1:] + [current]
        return window[-1]
