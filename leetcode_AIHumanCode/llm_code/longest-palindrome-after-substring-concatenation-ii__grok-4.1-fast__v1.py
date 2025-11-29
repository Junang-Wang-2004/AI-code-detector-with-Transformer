class Solution:
    def longestPalindrome(self, s, t):
        def compute_pal_prefixes(string):
            n = len(string)
            if n == 0:
                return [0]
            rs = string[::-1]
            MOD1 = 1000000007
            BASE1 = 131
            MOD2 = 1000000009
