class Solution:
    def superPow(self, a, b):
        mod = 1337
        exponent = 0
        for digit in b:
            exponent = exponent * 10 + digit
        return pow(a, exponent, mod)
