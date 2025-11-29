# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def resultsArray(self, nums, k):
        """
        """
        return [nums[i+k-1] if all(nums[j]+1 == nums[j+1] for j in range(i, i+k-1)) else -1 for i in range(len(nums)-k+1)]
