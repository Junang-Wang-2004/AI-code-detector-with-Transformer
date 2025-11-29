class Solution:
    def minimumSum(self, n):
        digits = []
        temp = n
        while temp:
            digits.append(temp % 10)
            temp //= 10
        digits.sort()
        first = second = 0
        for i, d in enumerate(digits):
            if i % 2 == 0:
                first = first * 10 + d
            else:
                second = second * 10 + d
        return first + second
