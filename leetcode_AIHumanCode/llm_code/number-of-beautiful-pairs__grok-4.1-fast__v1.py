class Solution(object):
    def countBeautifulPairs(self, nums):
        def gcd(u, v):
            if v == 0:
                return u
            return gcd(v, u % v)

        tally = [0] * 10
        pairs = 0
        for val in nums:
            s = str(val)
            start_digit = int(s[0])
            end_digit = int(s[-1])
            for digit in range(1, 10):
                if gcd(digit, end_digit) == 1:
                    pairs += tally[digit]
            tally[start_digit] += 1
        return pairs
