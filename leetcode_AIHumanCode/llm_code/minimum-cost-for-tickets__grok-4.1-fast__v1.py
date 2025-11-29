class Solution:
    def mincostTickets(self, days, costs):
        if not days:
            return 0
        travel_days = set(days)
        last_day = days[-1]
        dp = [float('inf')] * (last_day + 1)
        dp[0] = 0
        pass_lengths = [1, 7, 30]
        for day in range(1, last_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
                continue
            for idx, length in enumerate(pass_lengths):
                prev_day = max(0, day - length)
                dp[day] = min(dp[day], dp[prev_day] + costs[idx])
        return dp[last_day]
