import bisect

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        n = len(startTime)
        sched = [(startTime[k], endTime[k], profit[k]) for k in range(n)]
        sched.sort(key=lambda t: t[1])
        term_times = []
        best_profits = []
        top_profit = 0
        for begin, finish, gain in sched:
            pos = bisect.bisect_right(term_times, begin) - 1
            prior_best = best_profits[pos] if pos >= 0 else 0
            option = prior_best + gain
            updated = max(top_profit, option)
            term_times.append(finish)
            best_profits.append(updated)
            top_profit = updated
        return top_profit
