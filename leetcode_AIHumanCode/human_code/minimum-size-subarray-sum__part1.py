# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start = 0
        sum = 0
        min_size = float("inf")
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1

        return min_size if min_size != float("inf") else 0

