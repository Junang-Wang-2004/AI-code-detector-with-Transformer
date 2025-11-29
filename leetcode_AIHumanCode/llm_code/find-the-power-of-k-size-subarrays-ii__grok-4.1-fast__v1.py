class Solution(object):
    def resultsArray(self, nums, k):
        n = len(nums)
        ans = [-1] * (n - k + 1)
        seg_start = 0
        for j in range(1, n):
            if nums[j] != nums[j - 1] + 1:
                seg_len = j - seg_start
                if seg_len >= k:
                    for st in range(seg_start, j - k + 1):
                        ans[st] = nums[st + k - 1]
                seg_start = j
        seg_len = n - seg_start
        if seg_len >= k:
            for st in range(seg_start, n - k + 1):
                ans[st] = nums[st + k - 1]
        return ans
