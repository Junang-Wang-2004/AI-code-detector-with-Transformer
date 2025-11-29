class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        nums.sort()
        n = len(nums)
        import bisect
        med_start = bisect.bisect_left(nums, k)
        large_start = bisect.bisect_left(nums, 2 * k - 1)
        flags = [False] * n
        extras = 0
        h_rem = op1
        s_rem = op2
        p = n
        while h_rem > 0 and p > large_start:
            p -= 1
            v = nums[p]
            nums[p] = (v + 1) // 2
            h_rem -= 1
            if s_rem > 0:
                nums[p] -= k
                s_rem -= 1
        high_lim = p - 1
        p = med_start
        while s_rem > 0 and p <= high_lim:
            if k % 2 == 1 and nums[p] % 2 == 0:
                flags[p] = True
            nums[p] -= k
            s_rem -= 1
            p += 1
        low_end = p
        p = high_lim
        while h_rem > 0 and p >= low_end:
            v = nums[p]
            nums[p] = (v + 1) // 2
            h_rem -= 1
            if k % 2 == 1 and v % 2 == 1:
                extras += 1
            p -= 1
        opts = sorted((nums[i], i) for i in range(low_end))
        while h_rem > 0 and opts:
            v, i = opts.pop()
            nums[i] = (v + 1) // 2
            if extras > 0 and flags[i]:
                extras -= 1
                nums[i] -= 1
            h_rem -= 1
        return sum(nums)
