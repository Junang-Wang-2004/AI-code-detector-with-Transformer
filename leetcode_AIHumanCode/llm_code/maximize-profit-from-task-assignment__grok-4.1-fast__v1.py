class Solution:
    def maxProfit(self, workers, tasks):
        skill_count = {}
        for w in workers:
            skill_count[w] = skill_count.get(w, 0) + 1
        task_profits = {}
        for s, p in tasks:
            if s not in task_profits:
                task_profits[s] = []
            task_profits[s].append(p)
        total_profit = 0
        leftovers = []
        for skill, profits in task_profits.items():
            sorted_profits = sorted(profits, reverse=True)
            num_workers = skill_count.get(skill, 0)
            assign_count = min(num_workers, len(sorted_profits))
            total_profit += sum(sorted_profits[:assign_count])
            if len(sorted_profits) > num_workers:
                leftovers.extend(sorted_profits[assign_count:])
        if leftovers:
            total_profit += max(leftovers)
        return total_profit
