class Solution:
    def minimumIndex(self, nums):
        n = len(nums)
        if n == 0:
            return -1
        candidate = nums[0]
        count = 1
        for i in range(1, n):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1
        total = sum(x == candidate for x in nums)
        prefix = 0
        for j in range(n):
            if nums[j] == candidate:
                prefix += 1
            p_len = j + 1
            s_len = n - p_len
            s_count = total - prefix
            if prefix * 2 > p_len and s_count * 2 > s_len:
                return j
        return -1
