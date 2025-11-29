class Solution:
    def longestPalindrome(self, s, t):
        tr = t[::-1]
        
        def pal_prefix_lens(st):
            nn = len(st)
            mx = [1] * nn
            for c in range(nn):
                l, r = c, c
                while l >= 0 and r < nn and st[l] == st[r]:
                    mx[l] = max(mx[l], r - l + 1)
                    l -= 1
                    r += 1
                l, r = c, c + 1
                while l >= 0 and r < nn and st[l] == st[r]:
                    mx[l] = max(mx[l], r - l + 1)
                    l -= 1
                    r += 1
            return mx + [0]
        
        ext_s = pal_prefix_lens(s)
        ext_tr = pal_prefix_lens(tr)
        n, mm = len(s), len(tr)
        ans = 0
        dpp = [[0] * (mm + 1) for _ in range(2)]
        for ii in range(n):
            cur = ii % 2
            prv = 1 - cur
            dpp[cur][0] = 0
            for jj in range(mm):
                eq = s[ii] == tr[jj]
                dpp[cur][jj + 1] = dpp[prv][jj] + 2 if eq else 0
                sh = 1 if eq else 0
                ans = max(ans, dpp[cur][jj + 1] + ext_s[ii + sh])
                ans = max(ans, dpp[cur][jj + 1] + ext_tr[jj + sh])
        return ans
