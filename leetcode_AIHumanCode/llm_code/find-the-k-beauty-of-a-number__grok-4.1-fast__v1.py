class Solution:
    def divisorSubstrings(self, num, k):
        digits = str(num)
        length = len(digits)
        total = 0
        for pos in range(length - k + 1):
            window = int(digits[pos:pos + k])
            if window != 0 and num % window == 0:
                total += 1
        return total
