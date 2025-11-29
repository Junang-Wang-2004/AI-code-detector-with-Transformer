class Solution:
    def maximumOddBinaryNumber(self, s):
        count_one = 0
        for ch in s:
            if ch == '1':
                count_one += 1
        count_zero = len(s) - count_one
        return '1' * (count_one - 1) + '0' * count_zero + '1'
