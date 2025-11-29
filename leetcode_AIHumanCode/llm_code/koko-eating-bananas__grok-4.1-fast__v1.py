class Solution:
    def minEatingSpeed(self, piles, H):
        max_pile = max(piles)
        low, high = 1, max_pile
        
        def can_complete(bananas, hours, rate):
            needed = 0
            for b in bananas:
                needed += (b + rate - 1) // rate
            return needed <= hours
        
        while low < high:
            mid = (low + high) // 2
            if can_complete(piles, H, mid):
                high = mid
            else:
                low = mid + 1
        return low
