class Solution:
    def maxRunTime(self, computers, bat_cap):
        def possible(duration):
            total_usable = 0
            need = computers * duration
            for cap in bat_cap:
                total_usable += min(cap, duration)
                if total_usable >= need:
                    return True
            return total_usable >= need

        low = 0
        high = sum(bat_cap) // computers + 1 if computers > 0 else 0
        while low < high:
            mid = (low + high + 1) // 2
            if possible(mid):
                low = mid
            else:
                high = mid - 1
        return low
