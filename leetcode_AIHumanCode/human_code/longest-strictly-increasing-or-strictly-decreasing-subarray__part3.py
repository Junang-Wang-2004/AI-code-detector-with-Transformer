# Time:  O(n)
# Space: O(1)
# array
class Solution3(object):
    def longestMonotonicSubarray(self, nums):
        """
        """
        def f(compare):
            result = l = 0
            for i in range(len(nums)):
                l += 1
                if i+1 == len(nums) or not compare(nums[i], nums[i+1]):
                    result = max(result, l)
                    l = 0
            return result

        return max(f(lambda x, y: x < y), f(lambda x, y: x > y))
