class Solution(object):
    def splitArray(self, nums):
        if len(nums) < 7:
            return False
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        n = len(nums)
        total = prefix[n]
        for m in range(2, n - 1):
            left_total = prefix[m]
            if left_total * 2 != total:
                continue
            s = left_total // 2
            left_ok = any(prefix[p] == s for p in range(1, m))
            if not left_ok:
                continue
            target = total - s
            right_ok = any(prefix[p] == target for p in range(m + 1, n))
            if right_ok:
                return True
        return False
