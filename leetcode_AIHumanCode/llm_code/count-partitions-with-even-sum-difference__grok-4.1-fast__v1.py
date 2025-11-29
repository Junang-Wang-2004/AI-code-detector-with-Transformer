class Solution:
    def countPartitions(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        parity = 0
        for num in nums:
            parity = (parity + num) % 2
        return n - 1 if parity == 0 else 0
