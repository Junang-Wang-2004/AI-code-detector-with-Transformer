class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        ma = nums[0]
        mi = nums[0]
        for v in nums[1:]:
            p1 = ma * v
            p2 = mi * v
            new_ma = v
            new_mi = v
            if p1 > new_ma:
                new_ma = p1
            if p2 > new_ma:
                new_ma = p2
            if p1 < new_mi:
                new_mi = p1
            if p2 < new_mi:
                new_mi = p2
            ma = new_ma
            mi = new_mi
            if new_ma > res:
                res = new_ma
        return res
