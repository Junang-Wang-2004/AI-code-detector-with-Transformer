class Solution(object):
    def countWinningSequences(self, s):
        MOD = 10**9 + 7
        if not s:
            return 0
        n = len(s)
        offset = n
        cmap = {'F': 0, 'W': 1, 'E': 2}
        opp = [cmap[ch] for ch in s]
        prev_dp = [[0] * (2 * n + 1) for _ in range(3)]
        for j in range(3):
            delta = ((j - opp[0] + 1) % 3) - 1
            prev_dp[j][delta + offset] = 1
        for i in range(1, n):
            curr_dp = [[0] * (2 * n + 1) for _ in range(3)]
            for p in range(3):
                for d in range(2 * n + 1):
                    if prev_dp[p][d] == 0:
                        continue
                    sc = d - offset
                    for j in range(3):
                        if j == p:
                            continue
                        delta = ((j - opp[i] + 1) % 3) - 1
                        nd = sc + delta + offset
                        if 0 <= nd < 2 * n + 1:
                            curr_dp[j][nd] = (curr_dp[j][nd] + prev_dp[p][d]) % MOD
            prev_dp = curr_dp
        res = 0
        for j in range(3):
            for d in range(offset + 1, 2 * n + 1):
                res = (res + prev_dp[j][d]) % MOD
        return res
