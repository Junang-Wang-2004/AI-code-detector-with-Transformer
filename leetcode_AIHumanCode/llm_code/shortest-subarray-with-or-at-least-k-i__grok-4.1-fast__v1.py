class Solution:
    def minimumSubarrayLength(self, nums, k):
        all_or = 0
        for val in nums:
            all_or |= val
        if all_or < k:
            return -1
        
        counts = [0] * 32
        window_or = 0
        ans = len(nums) + 1
        j = 0
        for i in range(len(nums)):
            num = nums[i]
            for bit in range(32):
                if (1 << bit) & num:
                    counts[bit] += 1
                    if counts[bit] == 1:
                        window_or |= (1 << bit)
            while j <= i and window_or >= k:
                ans = min(ans, i - j + 1)
                left_num = nums[j]
                for bit in range(32):
                    if (1 << bit) & left_num:
                        counts[bit] -= 1
                        if counts[bit] == 0:
                            window_or &= ~(1 << bit)
                j += 1
        return ans if ans <= len(nums) else -1
