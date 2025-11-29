# Time:  O(nlogn)
# Space: O(n)
# greedy, sort
class Solution2(object):
    def maxAlternatingSum(self, nums):
        """
        """
        arr = sorted(x**2 for x in nums)
        return sum(arr)-2*sum(arr[i] for i in range(len(arr)//2))
