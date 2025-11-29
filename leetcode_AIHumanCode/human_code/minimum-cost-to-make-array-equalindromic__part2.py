# Time:  O(nlogn + logr)
# Space: O(logr)
# lc0564
# sort, math, string
class Solution2(object):
    def minimumCost(self, nums):
        """
        """
        def nearest_palindromic(x):
            n = str(x)
            l = len(n)
            result = {10**l+1, 10**(l-1)-1}
            prefix = int(n[:(l+1)/2])
            for i in map(str, (prefix-1, prefix, prefix+1)):
                result.add(int(i+[i, i[:-1]][l%2][::-1]))
            return result
    
        nums.sort()
        median = nums[len(nums)//2]
        if len(nums)%2 == 0:
            median = (median+nums[len(nums)//2-1])//2
        return min(sum(abs(x-p) for x in nums) for p in nearest_palindromic(median))
