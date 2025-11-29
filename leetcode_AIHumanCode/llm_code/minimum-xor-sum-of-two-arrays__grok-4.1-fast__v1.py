class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        memo = {}
        def dfs(pos, state):
            if pos == n:
                return 0
            key = (pos, state)
            if key in memo:
                return memo[key]
            result = float('inf')
            for k in range(n):
                if (state & (1 << k)) == 0:
                    result = min(result, nums1[pos] ^ nums2[k] + dfs(pos + 1, state | (1 << k)))
            memo[key] = result
            return result
        return dfs(0, 0)
