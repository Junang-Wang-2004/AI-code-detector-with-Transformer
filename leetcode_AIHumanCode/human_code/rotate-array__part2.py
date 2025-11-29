# Time:  O(n)
# Space: O(1)
from fractions import gcd


class Solution2(object):
    """
    """

    def rotate(self, nums, k):
        def apply_cycle_permutation(k, offset, cycle_len, nums):
            tmp = nums[offset]
            for i in range(1, cycle_len):
                nums[(offset + i * k) % len(nums)], tmp = tmp, nums[(offset + i * k) % len(nums)]
            nums[offset] = tmp

        k %= len(nums)
        num_cycles = gcd(len(nums), k)
        cycle_len = len(nums) / num_cycles
        for i in range(num_cycles):
            apply_cycle_permutation(k, i, cycle_len, nums)


