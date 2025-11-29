class Solution:
    def maximumTastiness(self, price, k):
        arr = sorted(price)
        if not arr:
            return 0

        def feasible(gap):
            count = 1
            prev = arr[0]
            for val in arr[1:]:
                if val - prev >= gap:
                    count += 1
                    prev = val
            return count >= k

        low = 0
        high = arr[-1] - arr[0]
        while low < high:
            mid = low + (high - low + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1
        return low
