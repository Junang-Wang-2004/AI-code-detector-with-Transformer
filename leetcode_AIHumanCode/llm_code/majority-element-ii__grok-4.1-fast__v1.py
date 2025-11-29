class Solution:
    def majorityElement(self, nums):
        maj1 = maj2 = None
        vote1 = vote2 = 0
        for num in nums:
            if maj1 == num:
                vote1 += 1
            elif maj2 == num:
                vote2 += 1
            elif vote1 == 0:
                maj1 = num
                vote1 = 1
            elif vote2 == 0:
                maj2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        vote1 = vote2 = 0
        n = len(nums)
        limit = n // 3
        for num in nums:
            if maj1 == num:
                vote1 += 1
            if maj2 == num:
                vote2 += 1
        result = []
        if vote1 > limit:
            result.append(maj1)
        if vote2 > limit:
            result.append(maj2)
        return result
