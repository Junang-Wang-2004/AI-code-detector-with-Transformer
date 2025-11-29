class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        max_profit = 0
        peak_run = -1
        total_profit = 0
        in_queue = 0
        operation = 0
        for arrivals in customers:
            in_queue += arrivals
            operation += 1
            boarded = min(4, in_queue)
            in_queue -= boarded
            total_profit += boarded * boardingCost - runningCost
            if total_profit > max_profit:
                max_profit = total_profit
                peak_run = operation
        while in_queue > 0:
            operation += 1
            boarded = min(4, in_queue)
            in_queue -= boarded
            total_profit += boarded * boardingCost - runningCost
            if total_profit > max_profit:
                max_profit = total_profit
                peak_run = operation
        return peak_run
