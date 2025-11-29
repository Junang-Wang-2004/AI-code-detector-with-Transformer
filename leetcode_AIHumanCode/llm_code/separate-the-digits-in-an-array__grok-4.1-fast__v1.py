class Solution:
    def separateDigits(self, nums):
        output = []
        for number in nums:
            buffer = []
            current = number
            while current:
                buffer.append(current % 10)
                current //= 10
            output.extend(buffer[::-1])
        return output
