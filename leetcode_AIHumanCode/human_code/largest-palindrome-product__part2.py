# Time:  O(10^(2n))
# Space: O(n)
class Solution2(object):
    def largestPalindrome(self, n):
        """
        """
        def divide_ceil(a, b):
            return (a+b-1)//b

        if n == 1:
            return 9
        upper, lower = 10**n-1, 10**(n-1)
        for i in reversed(range(lower, upper**2//(10**n)+1)):
            candidate = int(str(i) + str(i)[::-1])
            for y in reversed(range(divide_ceil(lower, 11)*11, upper+1, 11)):  # y must be divisible by 11 because even-number-length palindrome meets modulo 11 digit check
                if candidate//y > upper:
                    break
                if candidate%y == 0 and lower <= candidate//y:
                    return candidate%1337
        return -1
