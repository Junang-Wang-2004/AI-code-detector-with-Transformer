class Solution:
    def removeZeros(self, n):
        if n == 0:
            return 0
        highest_power = 1
        temp = n
        while temp >= 10:
            temp //= 10
            highest_power *= 10
        answer = 0
        while highest_power > 0:
            digit = (n // highest_power) % 10
            if digit != 0:
                answer = answer * 10 + digit
            highest_power //= 10
        return answer
