# Time:  O(nlogn)
# Space: O(n)
# prefix sum
class Solution3(object):
    def minCost(self, nums, cost):
        """
        """
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x])
        prefix = [0]*(len(cost)+1)
        left = 0
        for i in range(len(cost)):
            if i-1 >= 0:
                left += prefix[i]*(nums[idxs[i]]-nums[idxs[i-1]])
            prefix[i+1] = prefix[i]+cost[idxs[i]]
        result = float("inf")
        suffix = right = 0
        for i in reversed(range(len(cost))):
            if i+1 < len(idxs):
                right += suffix*(nums[idxs[i+1]]-nums[idxs[i]])
            result = min(result, left+right)
            if i-1 >= 0:
                left -= prefix[i]*(nums[idxs[i]]-nums[idxs[i-1]])
            suffix += cost[idxs[i]]
        return result
