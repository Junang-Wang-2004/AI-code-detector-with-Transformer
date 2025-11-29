class Solution:
    def removeBoxes(self, boxes):
        n = len(boxes)
        dp = [[[0] * (n + 1) for _ in range(n)] for _ in range(n)]
        for seg_len in range(1, n + 1):
            for start in range(n - seg_len + 1):
                end = start + seg_len - 1
                for bonus in range(n - seg_len + 1):
                    col = boxes[start]
                    streak_len = 1
                    while start + streak_len <= end and boxes[start + streak_len] == col:
                        streak_len += 1
                    streak_end = start + streak_len - 1
                    val = (bonus + streak_len) ** 2
                    if streak_end + 1 <= end:
                        val += dp[streak_end + 1][end][0]
                    for idx in range(streak_end + 1, end + 1):
                        if boxes[idx] == col:
                            mid_beg = streak_end + 1
                            mid_fin = idx - 1
                            mid_val = 0 if mid_beg > mid_fin else dp[mid_beg][mid_fin][0]
                            r_bonus = bonus + streak_len
                            r_val = dp[idx][end][r_bonus]
                            val = max(val, mid_val + r_val)
                    dp[start][end][bonus] = val
        return dp[0][n - 1][0]
