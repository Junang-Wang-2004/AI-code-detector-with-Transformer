class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums.sort()
        cnt = 0
        next_pos = -10**18
        for num in nums:
            if next_pos <= num + k:
                next_pos = max(next_pos, num - k) + 1
                cnt += 1
        return cnt
