class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dp(p, q):
            if p == len(s1) and q == len(s2):
                return True
            state = (p, q)
            if state in memo:
                return memo[state]
            pos = p + q
            ok = (p < len(s1) and s1[p] == s3[pos] and dp(p + 1, q)) or \
                 (q < len(s2) and s2[q] == s3[pos] and dp(p, q + 1))
            memo[state] = ok
            return ok
        return dp(0, 0)
