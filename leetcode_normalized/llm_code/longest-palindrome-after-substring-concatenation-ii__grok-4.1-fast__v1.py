class C1:

    def longestPalindrome(self, a1, a2):

        def compute_pal_prefixes(a1):
            v1 = len(a1)
            if v1 == 0:
                return [0]
            v2 = a1[::-1]
            v3 = 1000000007
            v4 = 131
            v5 = 1000000009
