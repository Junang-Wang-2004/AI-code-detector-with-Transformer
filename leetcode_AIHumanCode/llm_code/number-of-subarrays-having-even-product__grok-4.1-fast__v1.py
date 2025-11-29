class Solution:
    def evenProduct(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2
        odd_streak = 0
        odd_subs = 0
        for val in nums:
            if val % 2 != 0:
                odd_streak += 1
            else:
                odd_subs += odd_streak * (odd_streak + 1) // 2
                odd_streak = 0
        odd_subs += odd_streak * (odd_streak + 1) // 2
        return total - odd_subs
