class Solution:
    def minimumRelativeLosses(self, prices, queries):
        nums = sorted(prices)
        n = len(nums)
        prefix = [0]
        for val in nums:
            prefix.append(prefix[-1] + val)
        output = []
        for k, m in queries:
            left = 0
            right = m
            while left < right:
                center = (left + right) // 2
                hi_index = n - (m - center)
                if nums[center] + nums[hi_index] >= 2 * k:
                    right = center
                else:
                    left = center + 1
            lows = left
            highs = m - lows
            low_total = prefix[lows]
            high_total = prefix[n] - prefix[n - highs]
            loss = low_total + highs * k - (high_total - highs * k)
            output.append(loss)
        return output
