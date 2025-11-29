class Solution:
    def countDigitOne(self, n):
        count = 0
        place = 1
        while place <= n:
            next_place = place * 10
            prefix = n // next_place
            suffix = n % place
            digit = (n // place) % 10
            count += prefix * place
            if digit > 1:
                count += place
            elif digit == 1:
                count += suffix + 1
            place *= 10
        return count
