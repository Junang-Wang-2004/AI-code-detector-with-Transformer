class Solution(object):
    def addBinary(self, a, b):
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        digits = []
        for i in range(n - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            digits.append(str(total % 2))
            carry = total // 2
        if carry:
            digits.append('1')
        return ''.join(digits[::-1])
