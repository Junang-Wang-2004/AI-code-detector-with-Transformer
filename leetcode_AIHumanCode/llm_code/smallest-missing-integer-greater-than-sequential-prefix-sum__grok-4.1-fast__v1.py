class Solution(object):
    def missingInteger(self, nums):
        seen = set(nums)
        mex = 1
        while mex in seen:
            mex += 1
        return mex
