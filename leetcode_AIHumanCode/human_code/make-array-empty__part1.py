# Time:  O(nlogn)
# Space: O(n)

# sort
class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        """
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x])
        return len(idxs)+sum(len(idxs)-(i+1) for i in range(len(idxs)-1) if idxs[i] > idxs[i+1])


