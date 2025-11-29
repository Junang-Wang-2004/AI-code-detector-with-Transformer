import math

class Solution:
    def isGoodArray(self, nums):
        return math.gcd(*nums) == 1
