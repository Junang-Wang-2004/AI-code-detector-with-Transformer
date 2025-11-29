class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        cnt, left = 0, 0
        for right in range(len(nums)):
            if nums[right] - nums[left] > k:
                cnt += 1
                left = right
        return cnt + 1
