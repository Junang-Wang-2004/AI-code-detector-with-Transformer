class Solution(object):
    def superpalindromesInRange(self, L, R):
        def is_palindrome(n):
            s = str(n)
            return s == s[::-1]

        low = int(L)
        high = int(R)
        max_half = int(high ** 0.25) + 1
        ans = 0
        for i in range(1, max_half + 1):
            prefix = str(i)
            # odd-length palindromic root
            root1 = int(prefix + prefix[:-1][::-1])
            val1 = root1 * root1
            if low <= val1 <= high and is_palindrome(val1):
                ans += 1
            # even-length palindromic root
            root2 = int(prefix + prefix[::-1])
            val2 = root2 * root2
            if low <= val2 <= high and is_palindrome(val2):
                ans += 1
        return ans
