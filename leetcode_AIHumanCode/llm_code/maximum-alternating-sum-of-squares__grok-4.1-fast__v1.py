class Solution:
    def maxAlternatingSum(self, nums):
        sq = [val * val for val in nums]
        sq.sort(reverse=True)
        mid = (len(nums) + 1) // 2
        gain = sum(sq[:mid])
        loss = sum(sq[mid:])
        return gain - loss
