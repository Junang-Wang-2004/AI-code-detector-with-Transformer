class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        if not nums:
            return []
        highest = max(nums).bit_length()
        bits = max(highest, 1)
        last_pos = [-1] * bits
        res = [0] * n
        for i in range(n - 1, -1, -1):
            num = nums[i]
            b = 0
            while b < bits:
                mask = 1 << b
                if num & mask:
                    last_pos[b] = i
                b += 1
            farthest = max(last_pos)
            res[i] = max(farthest - i + 1, 1)
        return res
