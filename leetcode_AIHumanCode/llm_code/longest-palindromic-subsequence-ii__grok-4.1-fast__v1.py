class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        pal = [0] * n
        for idx in range(n):
            pal[idx] = 1
        for start in range(n - 2, -1, -1):
            diag_val = 0
            for end in range(start + 1, n):
                temp_val = pal[end]
                if s[start] == s[end]:
                    pal[end] = diag_val + 2
                else:
                    pal[end] = max(pal[end], pal[end - 1])
                diag_val = temp_val
        return pal[n - 1]
