# Time:  O(n * logr * logn)
# Space: O(nlogr)

# sort
class Solution(object):
    def maxGoodNumber(self, nums):
        """
        """
        return int("".join(sorted([bin(x)[2:] for x in nums], cmp=lambda x, y: (x+y > y+x)-(x+y < y+x), reverse=True)), 2)


