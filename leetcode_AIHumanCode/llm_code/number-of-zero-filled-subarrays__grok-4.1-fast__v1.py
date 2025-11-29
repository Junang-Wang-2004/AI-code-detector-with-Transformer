class Solution:
    def zeroFilledSubarray(self, nums):
        total = 0
        streak = 0
        for val in nums:
            if val == 0:
                streak += 1
            else:
                total += streak * (streak + 1) // 2
                streak = 0
        total += streak * (streak + 1) // 2
        return total
