class Solution(object):
    def largestInteger(self, num):
        digits = list(str(num))
        even_digits = sorted(int(d) for d in digits if int(d) % 2 == 0, reverse=True)
        odd_digits = sorted(int(d) for d in digits if int(d) % 2 == 1, reverse=True)
        even_idx = odd_idx = 0
        result = []
        for d in digits:
            if int(d) % 2 == 0:
                result.append(str(even_digits[even_idx]))
                even_idx += 1
            else:
                result.append(str(odd_digits[odd_idx]))
                odd_idx += 1
        return int(''.join(result))
