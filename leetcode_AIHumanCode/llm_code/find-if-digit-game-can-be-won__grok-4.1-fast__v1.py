class Solution:
    def canAliceWin(self, nums):
        total = sum(nums)
        small = sum(n for n in nums if n < 10)
        return 2 * small != total
