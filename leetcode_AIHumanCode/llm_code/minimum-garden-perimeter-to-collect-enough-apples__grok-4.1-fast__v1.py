class Solution:
    def minimumPerimeter(self, neededApples):
        lo = 0
        hi = 200000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * (2 * mid + 1) * (2 * mid + 2) >= neededApples:
                hi = mid
            else:
                lo = mid + 1
        return 8 * lo
