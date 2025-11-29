# Time:  O(nlogn)
# Space: O(n)
import bisect


# sort, prefix sum, greedy, binary search
class Solution4(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        """
        def check(prefix, total, x):
            return (prefix[x]-prefix[x-1])*x-prefix[x] <= total

        def binary_search_right(prefix, total, left, right):
            while left <= right:
                mid = left+(right-left)//2
                if not check(prefix, total, mid):
                    right = mid-1
                else:
                    left = mid+1
            return right
    
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+flowers[i]
        result = suffix = 0
        left = n
        for right in reversed(range(n+1)):
            if right != n:
                suffix += flowers[right]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                break
            left = binary_search_right(prefix, total, 1, right)
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result
