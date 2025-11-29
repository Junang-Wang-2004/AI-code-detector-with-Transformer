class Solution:
    def sumOfEncryptedInt(self, nums):
        def encrypt(num):
            digits = str(num)
            highest = max(int(d) for d in digits)
            ones_str = '1' * len(digits)
            return highest * int(ones_str)

        total = 0
        for number in nums:
            total += encrypt(number)
        return total
