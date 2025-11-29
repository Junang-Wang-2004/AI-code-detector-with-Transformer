class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        max_score = nums[k]
        min_val = nums[k]
        l, r = k, k
        while l > 0 or r < n - 1:
            if l == 0:
                r += 1
                min_val = min(min_val, nums[r])
            elif r == n - 1:
                l -= 1
                min_val = min(min_val, nums[l])
            else:
                if nums[l - 1] >= nums[r + 1]:
                    l -= 1
                    min_val = min(min_val, nums[l])
                else:
                    r += 1
                    min_val = min(min_val, nums[r])
            max_score = max(max_score, min_val * (r - l + 1))
        return max_score
