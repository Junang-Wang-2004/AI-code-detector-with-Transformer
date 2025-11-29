class Solution:
    def arrangeCoins(self, n):
        low, high = 0, n
        while low < high:
            mid = (low + high + 1) // 2
            if mid * (mid + 1) // 2 <= n:
                low = mid
            else:
                high = mid - 1
        return low
