class Solution:
    def maxProduct(self, num):
        first = -1
        second = -1
        while num > 0:
            dig = num % 10
            if dig > first:
                second = first
                first = dig
            elif dig > second:
                second = dig
            num //= 10
        if first == -1:
            return 1
        if second == -1:
            return first
        return first * second
