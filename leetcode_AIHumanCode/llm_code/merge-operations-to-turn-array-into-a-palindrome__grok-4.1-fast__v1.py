class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        i = 0
        j = len(nums) - 1
        sum_left = nums[i]
        sum_right = nums[j]
        while i < j:
            if sum_left < sum_right:
                i = i + 1
                sum_left = sum_left + nums[i]
                operations = operations + 1
            elif sum_right < sum_left:
                j = j - 1
                sum_right = sum_right + nums[j]
                operations = operations + 1
            else:
                i = i + 1
                j = j - 1
                if i < j:
                    sum_left = nums[i]
                    sum_right = nums[j]
        return operations
