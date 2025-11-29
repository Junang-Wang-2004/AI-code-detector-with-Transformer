class Solution:
    def maxOperations(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        candidates = {nums[0] + nums[1], nums[0] + nums[-1], nums[-2] + nums[-1]}
        result = 0
        for tgt in candidates:
            table = [[0] * n for _ in range(n)]
            for sz in range(2, n + 1):
                for begin in range(n - sz + 1):
                    finish = begin + sz - 1
                    best = 0
                    if nums[begin] + nums[begin + 1] == tgt:
                        best = max(best, 1 + (table[begin + 2][finish] if begin + 2 <= finish else 0))
                    if nums[begin] + nums[finish] == tgt:
                        best = max(best, 1 + (table[begin + 1][finish - 1] if begin + 1 <= finish - 1 else 0))
                    if nums[finish - 1] + nums[finish] == tgt:
                        best = max(best, 1 + (table[begin][finish - 2] if begin <= finish - 2 else 0))
                    table[begin][finish] = best
            result = max(result, table[0][n - 1])
        return result
