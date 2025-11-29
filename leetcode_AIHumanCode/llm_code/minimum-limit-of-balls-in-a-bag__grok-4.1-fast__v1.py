class Solution:
    def minimumSize(self, nums, maxOperations):
        def feasible(arr, ops, sz):
            return sum((n - 1) // sz for n in arr) <= ops
        
        low = 1
        high = max(nums)
        while low < high:
            m = (low + high) // 2
            if feasible(nums, maxOperations, m):
                high = m
            else:
                low = m + 1
        return low
