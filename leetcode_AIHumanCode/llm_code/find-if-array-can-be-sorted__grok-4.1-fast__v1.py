class Solution:
    def canSortArray(self, nums):
        def bitcount(n):
            cnt = 0
            while n:
                cnt += n & 1
                n >>= 1
            return cnt
        
        popc = [bitcount(x) for x in nums]
        m = len(nums)
        pos = 0
        prior_max = float('-inf')
        while pos < m:
            end = pos
            while end < m and popc[end] == popc[pos]:
                end += 1
            seg_min = min(nums[pos:end])
            if prior_max > seg_min:
                return False
            prior_max = max(nums[pos:end])
            pos = end
        return True
