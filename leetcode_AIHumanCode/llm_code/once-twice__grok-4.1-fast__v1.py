class Solution:
    def onceTwice(self, nums):
        ones, twos = 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        once_ones, once_twos = 0, 0
        for num in nums:
            if (num & ones) != ones or (num & twos):
                continue
            once_twos |= once_ones & num
            once_ones ^= num
            once_threes = once_ones & once_twos
            once_ones &= ~once_threes
            once_twos &= ~once_threes
        twice = (once_ones ^ ones) | twos
        return [once_ones, twice]
