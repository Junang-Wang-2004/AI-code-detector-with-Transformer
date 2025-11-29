class Solution(object):
    def canChoose(self, groups, nums):
        g = 0
        p = 0
        for x in nums:
            if g < len(groups) and x == groups[g][p]:
                p += 1
                if p == len(groups[g]):
                    g += 1
                    p = 0
        return g == len(groups)
