class Solution:
    def findLengthOfShortestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        suf_start = n
        for p in range(n - 2, -1, -1):
            if nums[p] > nums[p + 1]:
                suf_start = p + 1
                break
        
        if suf_start == 0:
            return 0
        
        max_pre = suf_start
        for k in range(1, suf_start):
            if nums[k] < nums[k - 1]:
                max_pre = k - 1
                break
        
        ans = suf_start
        j = suf_start
        for i in range(max_pre + 1):
            while j < n and nums[i] > nums[j]:
                j += 1
            ans = min(ans, j - i - 1)
        
        return ans
