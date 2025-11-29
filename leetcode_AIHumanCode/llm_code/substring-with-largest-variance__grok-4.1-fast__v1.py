class Solution(object):
    def largestVariance(self, s):
        chars = list(set(s))
        if len(chars) < 2:
            return 0
        n = len(s)
        SMALL = -2000000
        ans = 0
        for x in chars:
            for y in chars:
                if x == y:
                    continue
                dp = [SMALL] * 4
                local_max = SMALL
                for i in range(n):
                    delta = 1 if s[i] == x else -1 if s[i] == y else 0
                    bitx = 1 if s[i] == x else 0
                    bity = 1 if s[i] == y else 0
                    new_dp = [SMALL] * 4
                    idx_new = bitx * 2 + bity
                    new_dp[idx_new] = max(new_dp[idx_new], delta)
                    for prev in range(4):
                        if dp[prev] == SMALL:
                            continue
                        px = prev // 2
                        py = prev % 2
                        nx = px | bitx
                        ny = py | bity
                        nidx = nx * 2 + ny
                        nsum = dp[prev] + delta
                        new_dp[nidx] = max(new_dp[nidx], nsum)
                    dp = new_dp
                    local_max = max(local_max, dp[3])
                ans = max(ans, local_max)
        return ans
