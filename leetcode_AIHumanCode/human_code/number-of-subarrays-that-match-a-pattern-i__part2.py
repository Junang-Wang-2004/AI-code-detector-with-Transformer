# Time:  O(n * m)
# Space: O(1)
# brute force
class Solution2(object):
    def countMatchingSubarrays(self, nums, pattern):
        """
        """
        def check(i):
            return all(nums[i+j] == pattern[j] for j in range(len(pattern)))
    
        for i in range(len(nums)-1):
            nums[i] = cmp(nums[i+1], nums[i])
        return sum(check(i) for i in range(len(nums)-len(pattern)+1))
