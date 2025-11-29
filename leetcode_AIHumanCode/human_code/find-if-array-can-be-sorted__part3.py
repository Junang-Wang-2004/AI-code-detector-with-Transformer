# Time:  O(nlogn)
# Space: O(n)
# sort
class Solution3(object):
    def canSortArray(self, nums):
        """
        """
        def popcount(x):
            return bin(x).count("1")
    
        left = 0
        for right in range(len(nums)):
            if right+1 != len(nums) and popcount(nums[right+1]) == popcount(nums[right]):
                continue
            nums[left:right+1] = sorted(nums[left:right+1])
            left = right+1
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
