class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        indices = [idx for idx, val in enumerate(nums) if val == key]
        if not indices:
            return []
        ans = []
        left = max(0, indices[0] - k)
        right = min(len(nums) - 1, indices[0] + k)
        for idx in indices[1:]:
            new_left = max(0, idx - k)
            new_right = min(len(nums) - 1, idx + k)
            if new_left > right + 1:
                ans.extend(range(left, right + 1))
                left = new_left
                right = new_right
            else:
                right = max(right, new_right)
        ans.extend(range(left, right + 1))
        return ans
