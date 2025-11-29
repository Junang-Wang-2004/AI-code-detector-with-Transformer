class Solution:
    def makeTheIntegerZero(self, num1, num2):
        cnt = 0
        while cnt < 61:
            cnt += 1
            remainder = num1 - cnt * num2
            if remainder < 0:
                break
            bit_ones = bin(remainder).count('1')
            if bit_ones <= cnt <= remainder:
                return cnt
        return -1
