class Solution(object):
    def findMaxAverage(self, nums, k):
        low = min(nums)
        high = max(nums)
        for _ in range(60):
            mid = (low + high) / 2
            transformed = [0.0]
            current_sum = 0.0
            for val in nums:
                current_sum += val - mid
                transformed.append(current_sum)
            feasible = False
            window_min = 0.0
            for idx in range(k, len(transformed)):
                if idx - k > 0:
                    window_min = min(window_min, transformed[idx - k])
                if transformed[idx] >= window_min:
                    feasible = True
                    break
            if feasible:
                low = mid
            else:
                high = mid
        return low
