class Solution:
    def smallestFactorization(self, a):
        if a < 2:
            return a
        digits = []
        for d in range(9, 1, -1):
            while a % d == 0:
                digits.append(d)
                a //= d
        if a != 1:
            return 0
        digits.reverse()
        s = ''.join(str(x) for x in digits)
        val = int(s)
        return val if val < 2**31 else 0
