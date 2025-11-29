class Solution:
    def findMinimumTime(self, s, K):
        n = len(s)
        INF = 10**18 + 5
        memo = {}
        def rec(mask):
            if mask in memo:
                return memo[mask]
            if mask == 0:
                ans = 0
            else:
                bits = 0
                t = mask
                while t > 0:
                    bits += t & 1
                    t >>= 1
                divi = 1 + (bits - 1) * K
                ans = INF
                m = mask
                idx = 0
                while m > 0:
                    if m & 1:
                        p_mask = mask ^ (1 << idx)
                        p_val = rec(p_mask)
                        incr = (s[idx] + divi - 1) // divi
                        ans = min(ans, p_val + incr)
                    m >>= 1
                    idx += 1
            memo[mask] = ans
            return ans
        return rec((1 << n) - 1)
