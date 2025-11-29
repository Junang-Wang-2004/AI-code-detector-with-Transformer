class Solution:
    def countDistinctIntegers(self, nums):
        unique = set()
        for val in nums:
            unique.add(val)
            temp = val
            flipped = 0
            while temp > 0:
                flipped = flipped * 10 + temp % 10
                temp //= 10
            unique.add(flipped)
        return len(unique)
