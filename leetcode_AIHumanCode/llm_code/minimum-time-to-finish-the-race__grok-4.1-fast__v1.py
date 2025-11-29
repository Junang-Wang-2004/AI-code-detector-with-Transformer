class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        INF = 10**18
        max_streak = (changeTime + 1).bit_length() + 5
        streak_costs = [INF] * max_streak
        for f, r in tires:
            total = 0
            lap = f
            i = 0
            while lap < changeTime + f and i < max_streak:
                total += lap
                streak_costs[i] = min(streak_costs[i], total)
                lap *= r
                i += 1
        finish_times = [INF] * (numLaps + 1)
        finish_times[0] = 0
        for laps in range(1, numLaps + 1):
            for s in range(1, min(laps, max_streak) + 1):
                stint_time = streak_costs[s - 1]
                if stint_time == INF:
                    continue
                prior_laps = laps - s
                change_cost = changeTime if prior_laps > 0 else 0
                finish_times[laps] = min(finish_times[laps], finish_times[prior_laps] + change_cost + stint_time)
        return finish_times[numLaps]
