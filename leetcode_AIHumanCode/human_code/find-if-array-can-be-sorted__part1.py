# Time:  O(n)
# Space: O(1)

# sort
class Solution(object):
    def canSortArray(self, nums):
        """
        """
        def popcount(x):
            return bin(x).count("1")
    
        left = mx = 0
        for right in range(len(nums)):
            if right+1 != len(nums) and popcount(nums[right+1]) == popcount(nums[right]):
                continue
            if mx > min(nums[i] for i in range(left, right+1)):
                return False
            mx = max(nums[i] for i in range(left, right+1))
            left = right+1
        return True


