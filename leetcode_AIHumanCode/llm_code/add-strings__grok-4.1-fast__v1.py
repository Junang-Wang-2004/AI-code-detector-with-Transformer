class Solution:
    def addStrings(self, a, b):
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        result = ''
        carry = 0
        for x, y in zip(reversed(a), reversed(b)):
            total = int(x) + int(y) + carry
            result = str(total % 10) + result
            carry = total // 10
        while carry:
            result = str(carry % 10) + result
            carry //= 10
        return result
