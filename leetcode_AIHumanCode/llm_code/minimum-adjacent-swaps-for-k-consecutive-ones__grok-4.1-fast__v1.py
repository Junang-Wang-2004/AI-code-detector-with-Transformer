class Solution(object):
    def minMoves(self, nums, k):
        positions = [i for i, num in enumerate(nums) if num]
        n = len(positions)
        if n < k:
            return float('inf')
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + positions[i]
        half = k // 2
        adjust = half * ((k + 1) // 2)
        min_cost = float('inf')
        for i in range(n - k + 1):
            temp = psum[i + k] + psum[i] - psum[i + half] - psum[i + (k + 1) // 2]
            if temp < min_cost:
                min_cost = temp
        return min_cost - adjust
