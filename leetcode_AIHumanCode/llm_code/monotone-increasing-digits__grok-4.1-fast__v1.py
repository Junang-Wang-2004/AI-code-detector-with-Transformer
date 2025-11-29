class Solution(object):
    def monotoneIncreasingDigits(self, N):
        digits = list(str(N))
        length = len(digits)
        pos = length - 1
        while pos > 0:
            if int(digits[pos - 1]) <= int(digits[pos]):
                pos -= 1
            else:
                digits[pos - 1] = str(int(digits[pos - 1]) - 1)
                for j in range(pos, length):
                    digits[j] = '9'
                pos -= 1
        return int(''.join(digits))
