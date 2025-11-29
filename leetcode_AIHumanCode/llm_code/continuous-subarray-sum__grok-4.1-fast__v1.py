class Solution(object):
    def checkSubarraySum(self, nums, k):
        indices = {0: -1}
        running = 0
        pos = 0
        length = len(nums)
        while pos < length:
            running += nums[pos]
            if k != 0:
                running %= k
            if running in indices:
                if pos - indices[running] > 1:
                    return True
            else:
                indices[running] = pos
            pos += 1
        return False
