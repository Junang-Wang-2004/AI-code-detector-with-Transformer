class Solution(object):
    def perfectPairs(self, nums):
        vals = sorted(abs(x) for x in nums)
        total = 0
        ptr = 0
        n = len(vals)
        for i in range(n):
            while vals[i] > 2 * vals[ptr]:
                ptr += 1
            total += i - ptr
        return total
