class Solution(object):
    def largestPalindrome(self, n):
        if n == 1:
            return 9
        min_digit = 10 ** (n - 1)
        max_digit = 10 ** n - 1
        for left_part in range(max_digit, min_digit - 1, -1):
            palind = int(str(left_part) + str(left_part)[::-1])
            upper_d = min(max_digit, palind // min_digit)
            lower_d = max(min_digit, (palind + max_digit - 1) // max_digit)
            for d in range(upper_d, lower_d - 1, -1):
                if palind % d == 0:
                    return palind % 1337
        return -1
