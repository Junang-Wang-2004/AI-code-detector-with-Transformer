# Time:  O(nlogr)
# Space: O(1)

# binary search
class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        """
        def check(time, totalTrips, x):
            return sum(x//t for t in time) >= totalTrips

        left, right = 1, max(time)*totalTrips
        while left <= right:
            mid = left + (right-left)//2
            if check(time, totalTrips, mid):
                right = mid-1
            else:
                left = mid+1
        return left
