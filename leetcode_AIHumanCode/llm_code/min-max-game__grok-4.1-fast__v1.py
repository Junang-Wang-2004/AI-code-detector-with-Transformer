class Solution:
    def minMaxGame(self, nums):
        def recurse(pos, sz):
            if sz == 1:
                return
            h = sz // 2
            for j in range(h):
                x = nums[pos + 2 * j]
                y = nums[pos + 2 * j + 1]
                nums[pos + j] = min(x, y) if j % 2 == 0 else max(x, y)
            recurse(pos, h)
        m = len(nums)
        recurse(0, m)
        return nums[0]
