class Solution:
    def repairCars(self, rates, cars):
        min_rate = min(rates)
        low = 1
        high = min_rate * cars * cars
        
        def sufficient(time):
            total = 0
            for r in rates:
                total += int((time // r) ** 0.5)
                if total >= cars:
                    return True
            return total >= cars
        
        while low < high:
            mid = (low + high) // 2
            if sufficient(mid):
                high = mid
            else:
                low = mid + 1
        return low
