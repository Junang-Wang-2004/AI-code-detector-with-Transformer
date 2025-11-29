# Time:  O(nlogn)
# Space: O(1)
# sort, greedy
class Solution2(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        """
        nums.sort()
        return (sum(max(nums[i]-k, 0) for i in range(len(nums)//2+1))+
                sum(max(k-nums[i], 0) for i in range(len(nums)//2, len(nums))))
