# Time:  O(n + r)
# Space: O(n + r)

# sort
class Solution(object):
    def sortByAbsoluteValue(self, nums):
        """
        """
        mx = max(abs(x) for x in nums)
        lookup = [[] for _ in range(mx+1)]
        for x in nums:
            lookup[abs(x)].append(x)
        result = []
        for x in lookup:
            result.extend(x)
        return result


