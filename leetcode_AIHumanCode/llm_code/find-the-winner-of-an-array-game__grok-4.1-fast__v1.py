class Solution:
    def getWinner(self, nums, k):
        if len(nums) < 2:
            return nums[0] if nums else 0
        champion = nums[0]
        wins = 0
        pos = 1
        while pos < len(nums):
            if nums[pos] > champion:
                champion = nums[pos]
                wins = 1
            else:
                wins += 1
            if wins == k:
                return champion
            pos += 1
        return champion
