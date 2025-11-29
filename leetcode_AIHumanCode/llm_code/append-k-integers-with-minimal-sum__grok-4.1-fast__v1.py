class Solution:
    def minimalKSum(self, nums, k):
        vals = sorted(set(nums))
        total = 0
        start = 1
        idx = 0
        m = len(vals)
        while k > 0:
            if idx < m and vals[idx] == start:
                start += 1
                idx += 1
                continue
            total += start
            start += 1
            k -= 1
