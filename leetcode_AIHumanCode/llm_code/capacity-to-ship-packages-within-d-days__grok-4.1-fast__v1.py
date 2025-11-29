class Solution:
    def shipWithinDays(self, weights, D):
        def can_ship(pkgs, days, capacity):
            days_needed = 1
            load = 0
            for pkg in pkgs:
                if load + pkg > capacity:
                    days_needed += 1
                    load = pkg
                else:
                    load += pkg
            return days_needed <= days

        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            if can_ship(weights, D, mid):
                high = mid
            else:
                low = mid + 1
        return low
