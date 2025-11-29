class Solution:
    def maxPossibleScore(self, nums, limit):
        nums.sort()
        def possible(step):
            prev_pos = nums[0]
            for i in range(1, len(nums)):
                next_pos = max(prev_pos + step, nums[i])
                if next_pos > nums[i] + limit:
                    return False
                prev_pos = next_pos
            return True
        
        lo = 1
        hi = nums[-1] + limit - nums[0]
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
