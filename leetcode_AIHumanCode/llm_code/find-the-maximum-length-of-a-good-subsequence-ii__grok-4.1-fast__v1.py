class Solution:
    def maximumLength(self, nums, k):
        lasts = [{} for _ in range(k + 1)]
        best = [0] * (k + 1)
        for val in nums:
            prev_best = best[:]
            for cnt in range(k + 1):
                len_here = lasts[cnt].get(val, 0) + 1
                if cnt > 0:
                    len_here = max(len_here, prev_best[cnt - 1] + 1)
                lasts[cnt][val] = len_here
                best[cnt] = max(best[cnt], len_here)
        return best[k]
