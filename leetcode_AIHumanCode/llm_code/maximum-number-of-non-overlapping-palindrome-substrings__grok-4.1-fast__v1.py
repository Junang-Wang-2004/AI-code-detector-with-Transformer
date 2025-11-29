class Solution:
    def maxPalindromes(self, s, k):
        def find_next_start(ctr, low):
            l, r = divmod(ctr, 2)
            while l >= low and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= k:
                    return r + 1
                l -= 1
                r += 1
            return -1

        n = len(s)
        num = 0
        curr_low = 0
        for ctr in range(2 * n - 1):
            nxt_low = find_next_start(ctr, curr_low)
            if nxt_low != -1:
                curr_low = nxt_low
                num += 1
        return num
