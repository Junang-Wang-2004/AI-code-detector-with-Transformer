class Solution:
    def minDays(self, bloomDay, m, k):
        def feasible(days):
            bouquets, streak = 0, 0
            for time in bloomDay:
                if time <= days:
                    streak += 1
                    if streak == k:
                        bouquets += 1
                        streak = 0
                        if bouquets >= m:
                            return True
                else:
                    streak = 0
            return bouquets >= m

        n = len(bloomDay)
        if n < m * k:
            return -1
        
        low, high = 1, max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
