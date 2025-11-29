from functools import reduce
# Time:  O(nlogn + n * k)
# Space: O(n)
# sort, combinatorics
class Solution2(object):
    def minMaxSums(self, nums, k):
        """
        """
        MOD = 10**9+7
        nums.sort()
        result = 0
        cnt = 1
        for i in range(len(nums)):
            cnt = reduce(lambda accu, x: (accu+x)%MOD, (nCr(i, j) for j in range(min(i, k-1)+1)), 0)
            result = (result+(nums[i]+nums[~i])*cnt)%MOD
        return result
