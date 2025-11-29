class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        peak = max(nums)
        all_subs = n * (n + 1) // 2
        poor = 0
        ptr = 0
        tally = 0
        for idx in range(n):
            if nums[idx] == peak:
                tally += 1
            while tally > k - 1 and ptr <= idx:
                if nums[ptr] == peak:
                    tally -= 1
                ptr += 1
            poor += idx - ptr + 1
        return all_subs - poor
