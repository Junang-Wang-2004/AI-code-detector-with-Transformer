class Solution:
    def maximum69Number(self, num):
        highest = 1
        while highest * 10 <= num:
            highest *= 10
        while highest:
            digit = (num // highest) % 10
            if digit == 6:
                return num + 3 * highest
            highest //= 10
        return num
