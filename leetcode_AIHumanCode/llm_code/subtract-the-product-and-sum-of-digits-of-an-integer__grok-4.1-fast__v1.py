class Solution:
    def subtractProductAndSum(self, num):
        mult, add = 1, 0
        while num > 0:
            digit = num % 10
            mult *= digit
            add += digit
            num //= 10
        return mult - add
