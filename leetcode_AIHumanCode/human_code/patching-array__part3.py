# Time:  O(s + logn), s is the number of elements in the array
# Space: O(1)
class Solution3(object):
    def minPatches(self, nums, n):
        """
        """
        patch, miss, i = 0, 1, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patch += 1

        return patch

