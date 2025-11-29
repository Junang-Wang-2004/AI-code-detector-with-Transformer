class Solution(object):
    def longestCommonPrefix(self, s, t):
        p, q = 0, 0
        ans = 0
        while p < len(s) and q < len(t) and s[p] == t[q]:
            ans += 1
            p += 1
            q += 1
        if q == len(t):
            return ans
        p += 1
        while p < len(s) and q < len(t) and s[p] == t[q]:
            ans += 1
            p += 1
            q += 1
        return ans
