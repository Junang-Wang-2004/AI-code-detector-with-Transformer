class Solution(object):
    def minSizeSubarray(self, nums, target):
        n = len(nums)
        total = sum(nums)
        full_cycles = target // total
        remainder = target % total
        if remainder == 0:
            return full_cycles * n
        doubled = nums + nums
        prefix = [0]
        for num in doubled:
            prefix.append(prefix[-1] + num)
        pos = {0: 0}
        ans = float('inf')
        for i in range(1, 2 * n + 1):
            curr_prefix = prefix[i]
            if curr_prefix - remainder in pos:
                length_here = i - pos[curr_prefix - remainder]
                if length_here <= n:
                    ans = min(ans, length_here)
            pos[curr_prefix] = i
        return full_cycles * n + ans if ans != float('inf') else -1
