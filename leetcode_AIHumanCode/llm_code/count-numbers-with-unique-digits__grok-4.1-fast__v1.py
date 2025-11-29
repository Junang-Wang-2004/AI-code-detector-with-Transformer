class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        total = 1
        tail_prod = 1
        total += 9 * tail_prod
        for length in range(2, n + 1):
            tail_prod *= 11 - length
            total += 9 * tail_prod
        return total
