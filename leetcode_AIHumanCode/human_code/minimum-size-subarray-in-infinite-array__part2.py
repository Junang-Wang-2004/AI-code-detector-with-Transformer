# Time:  O(n)
# Space: O(n)
# prefix sum, hash table
class Solution2(object):
    def minSizeSubarray(self, nums, target):
        """
        """
        INF = float("inf")
        q, target = divmod(target, sum(nums))
        if not target:
            return q*len(nums)
        result = INF
        lookup = {0:-1}
        prefix = 0
        for right in range((len(nums)-1)+(len(nums)-1)):
            prefix += nums[right%len(nums)]
            if prefix-target in lookup:
                result = min(result, right-lookup[prefix-target])
            lookup[prefix] = right
        return result+q*len(nums) if result != INF else -1
