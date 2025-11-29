# Time:  O(mx * log(mn * c^2)) = O(mx * (logc + log(mn))), c = cars, mx = max(ranks), mn = min(ranks)
# Space: O(mx)

import collections


# freq table, binary search
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        """
        def check(x):
            return sum(int((x//k)**0.5)*v for k, v in cnt.items()) >= cars

        cnt = collections.Counter(ranks)
        left, right = 1, min(cnt.keys())*cars**2
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left


