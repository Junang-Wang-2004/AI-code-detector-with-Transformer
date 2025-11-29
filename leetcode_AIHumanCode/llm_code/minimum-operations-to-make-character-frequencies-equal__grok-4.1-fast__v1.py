class Solution(object):
    def makeStringGood(self, s):
        n = len(s)
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        ans = n
        positives = [f for f in freq if f > 0]
        if not positives:
            return ans
        min_target = min(positives)
        max_target = max(freq)
        INF = n + 1
        for target in range(min_target, max_target + 1):
            dp = [[INF] * 2 for _ in range(27)]
            dp[0][0] = dp[0][1] = 0
            for pos in range(1, 27):
                let = pos - 1
                count = freq[let]
                prv_free = 0
                if let > 0:
                    pcount = freq[let - 1]
                    prv_free = pcount - target if pcount >= target else pcount
                p_insert = dp[pos - 1][0]
                p_delete = dp[pos - 1][1]
                p_min = min(p_insert, p_delete)
                if count == 0:
                    dp[pos][0] = p_insert
                    dp[pos][1] = p_delete
                    continue
                if count >= target:
                    dp[pos][0] = INF
                    dp[pos][1] = p_min + count - target
                else:
                    need = target - count
                    keep_insert = min(p_min + need, p_delete + max(0, need - prv_free))
                    drop_delete = p_min + count
                    dp[pos][0] = keep_insert
                    dp[pos][1] = drop_delete
            curr_min = min(dp[26][0], dp[26][1])
            ans = min(ans, curr_min)
        return ans
