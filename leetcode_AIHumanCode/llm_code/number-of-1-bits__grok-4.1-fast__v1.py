class Solution:
    def hammingWeight(self, num: int) -> int:
        count = 0
        while num:
            count += num % 2
            num //= 2
        return count
