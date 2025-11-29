class Solution:
    def maxBalancedSubsequenceSum(self, nums):
        n = len(nums)
        INF = float('-inf')
        offsets = sorted({nums[i] - i for i in range(n)})
        m = len(offsets)
        pos = {offsets[i]: i + 1 for i in range(m)}
        tree = [INF] * (m + 2)
        
        def modify(idx, value):
            while idx <= m:
                tree[idx] = max(tree[idx], value)
                idx += idx & -idx
        
        def prefix_max(idx):
            result = INF
            while idx > 0:
                result = max(result, tree[idx])
                idx -= idx & -idx
            return result
        
        for i in range(n):
            num = nums[i]
            key = num - i
            rk = pos[key]
            prior = prefix_max(rk)
            current = max(prior, 0) + num
            modify(rk, current)
        
        return prefix_max(m)
