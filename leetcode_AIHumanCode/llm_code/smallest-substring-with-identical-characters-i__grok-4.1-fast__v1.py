class Solution:
    def minLength(self, s, numOps):
        n = len(s)
        def possible(max_run):
            if max_run == 1:
                mis = 0
                for i in range(n):
                    if int(s[i]) != (i % 2):
                        mis += 1
                return min(mis, n - mis) <= numOps
            ops_needed = 0
            run = 1
            for i in range(1, n):
                if s[i] == s[i - 1]:
                    run += 1
                else:
                    ops_needed += run // (max_run + 1)
                    run = 1
            ops_needed += run // (max_run + 1)
            return ops_needed <= numOps
        left, right = 1, n
        while left < right:
            pivot = (left + right) // 2
            if possible(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left
