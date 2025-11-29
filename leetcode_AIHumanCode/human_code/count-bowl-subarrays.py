# Time:  O(n)
# Space: O(n)

# mono stack
class Solution(object):
    def bowlSubarrays(self, nums):
        """
        """
        result = 0
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
                if stk:
                    result += 1
            stk.append(i)
        return result
