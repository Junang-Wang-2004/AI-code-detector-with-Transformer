class Solution:
    def minimizeMax(self, nums, p):
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        
        def feasible(threshold):
            count = 0
            pos = 0
            n = len(nums)
            while pos < n - 1 and count < p:
                if nums[pos + 1] - nums[pos] <= threshold:
                    count += 1
                    pos += 2
                else:
                    pos += 1
            return count >= p
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
