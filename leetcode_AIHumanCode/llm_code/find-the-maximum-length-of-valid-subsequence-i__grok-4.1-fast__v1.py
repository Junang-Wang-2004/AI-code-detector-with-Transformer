class Solution:
    def maximumLength(self, nums):
        even_cnt = odd_cnt = run_cnt = 0
        prev_p = -1
        for num in nums:
            p = num % 2
            if p == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
            if p != prev_p:
                run_cnt += 1
                prev_p = p
        return max(even_cnt, odd_cnt, run_cnt)
