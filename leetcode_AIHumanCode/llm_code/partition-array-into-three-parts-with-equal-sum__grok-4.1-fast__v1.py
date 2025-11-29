class Solution:
    def canThreePartsEqualSum(self, nums):
        total = sum(nums)
        if total % 3 != 0:
            return False
        target = total // 3
        prefix = 0
        seen_first = False
        for num in nums:
            prefix += num
            if prefix == target:
                seen_first = True
            if prefix == 2 * target and seen_first:
                return True
        return False
