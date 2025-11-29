class Solution:
    def minOperations(self, nums, x, y):
        if not nums:
            return 0
        max_k = 0
        for val in nums:
            max_k = max(max_k, (val + y - 1) // y)
        
        def compute_cost(k):
            extra = 0
            for val in nums:
                remaining = val - k * y
                if remaining > 0:
                    extra += (remaining + x - 1) // x
            return k + extra
        
        low = 0
        high = max_k
        while high - low >= 3:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            cost1 = compute_cost(mid1)
            cost2 = compute_cost(mid2)
            if cost1 <= cost2:
                high = mid2
            else:
                low = mid1
        
        result = float('inf')
        for k in range(low, high + 1):
            result = min(result, compute_cost(k))
        return result
