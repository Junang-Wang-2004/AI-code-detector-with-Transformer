import collections

class Solution(object):
    def minTravelTime(self, l, n, k, position, time):
        cumsum = [0] * (n + 1)
        for idx in range(n):
            cumsum[idx + 1] = cumsum[idx] + time[idx]
        travel_dp = [collections.defaultdict(lambda: float('inf')) for _ in range(n)]
        travel_dp[0][time[0]] = 0
        for curr in range(1, n):
            prev_start = max(0, curr - k - 1)
            for prev in range(prev_start, curr):
                for mult, cost_so_far in travel_dp[prev].items():
                    seg_sum = cumsum[curr + 1] - cumsum[prev + 1]
                    dist_cost = (position[curr] - position[prev]) * mult
                    total_cost = cost_so_far + dist_cost
                    travel_dp[curr][seg_sum] = min(travel_dp[curr][seg_sum], total_cost)
        return min(travel_dp[n - 1].values())
