class Solution:
    def minimumDistance(self, nums):
        pos = {}
        for idx, val in enumerate(nums):
            if val not in pos:
                pos[val] = []
            pos[val].append(idx)
        ans = float('inf')
        for indices in pos.values():
            n = len(indices)
            if n >= 3:
                for k in range(2, n):
                    ans = min(ans, 2 * (indices[k] - indices[k - 2]))
        return ans if ans != float('inf') else -1
