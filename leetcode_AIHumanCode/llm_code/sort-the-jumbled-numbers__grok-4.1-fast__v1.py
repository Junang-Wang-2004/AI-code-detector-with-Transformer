class Solution:
    def sortJumbled(self, mapping, nums):
        def remap(num):
            value = 0
            factor = 1
            for digit_char in str(num)[::-1]:
                digit = int(digit_char)
                value += mapping[digit] * factor
                factor *= 10
            return value

        order = sorted(range(len(nums)), key=lambda idx: remap(nums[idx]))
        return [nums[i] for i in order]
