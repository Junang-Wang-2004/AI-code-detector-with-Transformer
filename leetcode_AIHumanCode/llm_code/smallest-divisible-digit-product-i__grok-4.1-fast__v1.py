class Solution:
    def smallestNumber(self, n, t):
        current = n
        while True:
            prod = 1
            zero_mod = False
            for digit_char in str(current):
                prod = (prod * int(digit_char)) % t
                if prod == 0:
                    zero_mod = True
                    break
            if zero_mod:
                return current
            current += 1
